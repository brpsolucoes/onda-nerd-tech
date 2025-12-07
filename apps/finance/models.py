from apps.accounts.models import Company
from apps.accounts.context import get_current_company
from apps.finance.managers import TransactionManager
from apps.shared.models import BaseModel
from apps.shared.managers import CompanyManager

from datetime import datetime

from django.db import models


class Transaction(BaseModel):

    class TransactionTypeChoices(models.TextChoices):
        IN = 'income', 'Entrada'
        OUT = 'outcome', 'Saída'

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Empresa',
        related_name='transactions',
        blank=True,
        null=True,
    )
    title = models.CharField('Título', max_length=255)
    value = models.DecimalField('Valor', decimal_places=2, max_digits=10)
    due_date = models.DateField('Data de vencimento', blank=True, null=True)
    payment_date = models.DateTimeField('Data/Hora do pagamento', blank=True, null=True)
    is_paid = models.BooleanField('Está pago?', default=False)
    transaction_type = models.CharField('Tipo de transação',
                                        max_length=10,
                                        choices=TransactionTypeChoices.choices,
                                        default=TransactionTypeChoices.IN)
    is_installment = models.BooleanField('É parcela?', default=False)
    installment_number = models.PositiveIntegerField('Número da Parcela', null=True, blank=True)
    parent_transaction = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='installments',
        verbose_name='Transação Principal'
    )

    objects = CompanyManager()
    unfiltered_objects = models.Manager()
    services = TransactionManager()

    class Meta:
        ordering = ['due_date']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'

    def __str__(self):
        return f'{self.transaction_type} - {self.title}: R$ {self.value}'
    
    def save(self, *args, **kwargs):
        if not self.company_id:
            current_company_id = get_current_company()
            
            if current_company_id:
                self.company_id = current_company_id
            else:
                raise Exception("Não é possível salvar a transação. Nenhuma empresa ativa definida no contexto da requisição.")
        
        super().save(*args, **kwargs)

    def toggle_paid(self):
        is_paid = not self.is_paid
        if not is_paid:
            self.payment_date = None
        else:
            self.payment_date = datetime.now()
        self.is_paid = is_paid
        self.save(update_fields=['is_paid', 'payment_date'])
