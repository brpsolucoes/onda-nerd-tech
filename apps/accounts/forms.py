from apps.accounts.models import Company

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CompanyDataForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 
            'cnpj', 
            'state_registration', 
            'email', 
            'pix_key', 
            'access_credentials'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'state_registration': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pix_key': forms.TextInput(attrs={'class': 'form-control'}),
            'access_credentials': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['disabled'] = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['disabled'] = True
        self.fields['last_name'].widget.attrs['disabled'] = True
