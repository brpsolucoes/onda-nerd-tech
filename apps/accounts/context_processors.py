from apps.accounts.models import Company


def company_context(request):
    """
    Injeta a lista de empresas do usuário e a empresa ativa no contexto de todos os templates.
    """
    context = {}

    if request.user.is_authenticated:
        user_companies = request.user.company_set.all()
        
        active_company_id = request.session.get('active_company_id')
        
        active_company = None
        
        if active_company_id:
            try:
                active_company = Company.objects.get(pk=active_company_id)
            except Company.DoesNotExist:
                del request.session['active_company_id']

        context = {
            'user_companies': user_companies,
            'active_company': active_company,
            'active_company_id': active_company_id,
        }
        
    return context
