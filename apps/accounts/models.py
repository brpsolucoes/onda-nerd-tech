from apps.shared.models import BaseModel

from django.contrib.auth.models import User
from django.db import models


class Company(BaseModel):
    name = models.CharField('Nome da empresa', max_length=255)
    document = models.CharField('CNPJ da empresa', max_length=14, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True, blank=True, null=True)
    state_registration = models.CharField('Inscrição Estadual (IE)', max_length=30, blank=True, null=True)
    email = models.EmailField('E-mail Oficial', max_length=255, blank=True, null=True)
    pix_key = models.CharField('Chave PIX', max_length=255, blank=True, null=True)
    access_credentials = models.TextField('Acessos/Senhas (Notas)', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.name
