from apps.accounts.context import set_current_company, set_current_user_is_superuser
from apps.accounts.models import Company


class CompanyMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            set_current_user_is_superuser(request.user.is_superuser) 
            
            company_id = request.session.get('active_company_id')
            
            if company_id:
                set_current_company(company_id)
            elif not company_id and not request.user.is_superuser:
                try:
                    first_company = request.user.company_set.first()
                    if first_company:
                        request.session['active_company_id'] = first_company.pk
                        set_current_company(first_company.pk)
                except:
                    set_current_company(None)
        
        response = self.get_response(request)
        return response