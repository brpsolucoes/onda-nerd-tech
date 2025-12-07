from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.utils import timezone
from apps.finance.models import Transaction

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'shared/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        now = timezone.now()
        
        transactions = Transaction.objects.filter(
            due_date__month=now.month,
            due_date__year=now.year,
        )

        context['total_transactions'] = transactions.count()

        income = transactions.filter(transaction_type='income').aggregate(
            models.Sum('value')
        )['value__sum'] or 0
        
        outcome = transactions.filter(transaction_type='outcome').aggregate(
            models.Sum('value')
        )['value__sum'] or 0
        
        context['balance'] = income - outcome
        
        return context