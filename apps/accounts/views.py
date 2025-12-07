# apps/companies/views.py

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from .models import Company

@login_required
def switch_company(request, company_pk):
    """
    Permite ao usuário alternar para uma empresa que ele tem acesso.
    Reseta a paginação ao redirecionar.
    """
    company = get_object_or_404(
        Company.objects.filter(users=request.user), 
        pk=company_pk
    )
    request.session['active_company_id'] = company.pk
    next_url = request.META.get('HTTP_REFERER') or '/'
    parsed_url = urlparse(next_url)
    query_params = parse_qs(parsed_url.query)
    
    if 'page' in query_params:
        del query_params['page']
        
    new_query = urlencode(query_params, doseq=True)
    new_url = urlunparse(
        parsed_url._replace(query=new_query)
    )
    return redirect(new_url)
