from apps.accounts import views

from django.urls import include, path


app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('switch/<int:company_pk>/', views.switch_company, name='switch_company')
]
