from django.contrib import admin
from django.contrib.auth.models import Group
from apps.accounts.models import Company

admin.site.unregister(Group)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
