from django.db import models

from apps.accounts.context import get_current_company, get_current_user_is_superuser 


class CompanyQuerySet(models.QuerySet):
    def for_current_company(self):
        
        if get_current_user_is_superuser():
            return self.all() 

        company_id = get_current_company()
        if company_id:
            return self.filter(company_id=company_id)
            
        return self.none()


class CompanyManager(models.Manager):
    def get_queryset(self):
        return CompanyQuerySet(self.model, using=self._db).for_current_company()
        
    def all_companies(self):
        return CompanyQuerySet(self.model, using=self._db)