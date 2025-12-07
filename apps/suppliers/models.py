from apps.shared.models import BaseModel
from django.db import models


class Supplier(BaseModel):
    name = models.CharField('Nome do Fornecedor', max_length=255, unique=True)
    contact_name = models.CharField('Pessoa de Contato', max_length=255, blank=True, null=True)
    phone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    email = models.EmailField('Email', max_length=255, blank=True, null=True)
    cnpj = models.CharField('CNPJ/CPF', max_length=18, unique=True, blank=True, null=True)
    notes = models.TextField('Observações', blank=True, null=True)

    objects = models.Manager() 
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    def __str__(self):
        return self.name
