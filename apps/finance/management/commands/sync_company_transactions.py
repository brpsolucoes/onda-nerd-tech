from django.core.management.base import BaseCommand, CommandError
from django.db.models import F, Q

from apps.accounts.models import Company 
from apps.finance.models import Transaction


class Command(BaseCommand):
    help = 'Vincula todas as transações sem empresa (company=null) à primeira empresa cadastrada no sistema.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando vinculação de transações à primeira empresa...'))

        try:
            first_company = Company.objects.first()
            if not first_company:
                raise CommandError('Nenhuma empresa cadastrada no sistema. Crie a primeira empresa antes de rodar este comando.')

            self.stdout.write(self.style.SUCCESS(f'Empresa alvo encontrada: "{first_company.name}" (ID: {first_company.pk})'))

            transactions_to_update = Transaction.unfiltered_objects.filter(company__isnull=True)
            count = transactions_to_update.count()

            if count == 0:
                self.stdout.write(self.style.WARNING('Nenhuma transação sem vínculo encontrada. Operação concluída.'))
                return

            self.stdout.write(self.style.NOTICE(f'Encontradas {count} transações a serem vinculadas...'))

            updated_count = transactions_to_update.update(company=first_company)

            if updated_count == count:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Sucesso! {updated_count} transações vinculadas à empresa "{first_company.name}".'
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f'⚠️ Atenção! Ocorreu um erro no update. Esperado {count} atualizações, mas apenas {updated_count} foram realizadas.'
                    )
                )

        except CommandError as e:
            self.stdout.write(self.style.ERROR(e))
            self.stdout.write(self.style.ERROR('❌ O comando falhou.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))
            self.stdout.write(self.style.ERROR('❌ O comando falhou.'))
