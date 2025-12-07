from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'weight', 
            'width', 
            'height', 
            'depth', 
            'filament_consumption'
        ]
        labels = {
            'filament_consumption': 'Consumo de Filamento (gramas)',
            'weight': 'Peso Total (kg)', 
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'width': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'depth': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'filament_consumption': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
