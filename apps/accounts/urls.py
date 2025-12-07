from apps.accounts import views

from django.urls import include, path


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('switch/<int:company_pk>/', views.switch_company, name='switch_company'),
    path('settings/', views.SettingsDashboardView.as_view(), name='settings'),
    path('settings/company-data/', views.CompanyDataUpdateView.as_view(), name='company_data'),
    path('settings/password/', views.UserPasswordChangeView.as_view(), name='password_change'),
]
