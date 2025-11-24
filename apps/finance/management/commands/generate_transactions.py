import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from apps.finance.models import Transaction

# Configuração
NUM_TRANSACTIONS = 500

class Command(BaseCommand):
    help = f'Gera {NUM_TRANSACTIONS} transações de teste (income/outcome) para fins de paginação.'

    def handle(self, *args, **options):
        # Inicializa o Faker
        fake = Faker('pt_BR')
        
        # Limpa transações existentes (opcional, para garantir um teste limpo)
        # Transaction.objects.all().delete()
        # self.stdout.write(self.style.WARNING('Transações existentes excluídas.'))
        
        self.stdout.write(f'Iniciando a criação de {NUM_TRANSACTIONS} transações...')
        
        transactions_to_create = []
        now = timezone.now()
        
        for i in range(NUM_TRANSACTIONS):
            # Escolhe o tipo e o status de pagamento
            is_income = random.choice([True, False])
            is_paid = random.choice([True, False])

            # Gera datas aleatórias nos últimos 180 dias
            days_ago = random.randint(1, 180)
            due_date = now.date() - timedelta(days=days_ago)
            
            # Define o valor
            value = random.uniform(10.0, 5000.0)
            
            # Cria o objeto Transaction
            transaction = Transaction(
                title=fake.catch_phrase(),
                value=round(value, 2),
                due_date=due_date,
                is_paid=is_paid,
                transaction_type=Transaction.TransactionTypeChoices.IN if is_income else Transaction.TransactionTypeChoices.OUT,
            )
            
            # Define a data de pagamento se estiver pago
            if is_paid:
                payment_days_delay = random.randint(0, 10)
                transaction.payment_date = timezone.datetime.combine(
                    due_date + timedelta(days=payment_days_delay),
                    timezone.now().time()
                )
            
            transactions_to_create.append(transaction)

        # Cria os objetos em lote para melhor performance
        Transaction.objects.bulk_create(transactions_to_create)
        
        self.stdout.write(self.style.SUCCESS(f'\n{NUM_TRANSACTIONS} transações criadas com sucesso!'))