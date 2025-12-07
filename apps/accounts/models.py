from apps.shared.models import BaseModel

from django.contrib.auth.models import User
from django.db import models


class Company(BaseModel):
    name = models.CharField('Nome da empresa', max_length=255)
    document = models.CharField('CNPJ da empresa', max_length=14, blank=True, null=True)
    users = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.name
