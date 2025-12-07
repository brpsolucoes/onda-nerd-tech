from apps.accounts.models import Company
from apps.accounts.forms import CompanyDataForm, UserProfileForm
from apps.accounts.context import get_current_company

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView, TemplateView
from django.urls import reverse_lazy

from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


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


class CompanyDataUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyDataForm
    template_name = 'accounts/company_data_form.html'
    success_url = reverse_lazy('accounts:company_data') # Redireciona para a própria página

    def get_object(self, queryset=None):
        company_id = get_current_company()
        if not company_id:
            # Se não houver empresa ativa, redireciona ou levanta erro
            raise Http404("Nenhuma empresa ativa selecionada na sessão.")
            
        # Garante que o usuário tem acesso à empresa que está editando
        return get_object_or_404(
            Company.objects.filter(users=self.request.user), 
            pk=company_id
        )


class SettingsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/settings_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # O Context Processor já injeta user_companies e active_company
        context['form'] = UserProfileForm(instance=self.request.user)
        return context


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('accounts:settings')
