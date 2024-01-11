from django import forms

from .models import Clients, Cargos, Orders


class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name_client', 'number_telephone', 'email']
        widgets = {
            'name_client': forms.TextInput(attrs={'placeholder': "Имя"}),
            'number_telephone': forms.TextInput(attrs={'type': 'tel', 'placeholder': "Телефон"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"})
        }


class CargoInfoForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = ['name_cargo', 'type', 'weight', 'dimensions', 'type_transportation']
        widgets = {
            'name_cargo': forms.TextInput(attrs={'placeholder': "Название груза"}),
            'type': forms.TextInput(attrs={'placeholder': "Тип груза"}),
            'weight': forms.TextInput(attrs={'placeholder': "Вес груза"}),
            'dimensions': forms.TextInput(attrs={'placeholder': "Габариты груза"}),
            'type_transportation': forms.TextInput(attrs={'placeholder': "Тип перевозки"})
        }


class PriceInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['price_order']
        widgets = {
            'price_order': forms.TextInput(attrs={'disabled': True, 'values': '0р.'})
        }
