from apps.shared.models import BaseModel
from apps.shared.managers import CompanyManager 
from apps.accounts.models import Company 
from apps.accounts.context import get_current_company 

from django.db import models


class Product(BaseModel):
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Empresa',
        related_name='products',
    )
    name = models.CharField('Nome do Produto', max_length=255)
    weight = models.DecimalField('Peso Total do Produto (kg)', max_digits=10, decimal_places=3, default=0)
    width = models.DecimalField('Largura (cm)', max_digits=10, decimal_places=2, default=0)
    height = models.DecimalField('Altura (cm)', max_digits=10, decimal_places=2, default=0)
    depth = models.DecimalField('Profundidade (cm)', max_digits=10, decimal_places=2, default=0)
    filament_consumption = models.DecimalField(
        'Consumo de Filamento (gramas)', 
        max_digits=10, 
        decimal_places=2, 
        default=0,
        help_text='Consumo de filamento em peso (gramas) necessário para a produção.'
    )

    objects = CompanyManager() 
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.company_id:
            current_company_id = get_current_company()
            if current_company_id:
                self.company_id = current_company_id
            else:
                raise Exception("Não é possível salvar o produto sem uma empresa definida no contexto.")
        
        super().save(*args, **kwargs)
