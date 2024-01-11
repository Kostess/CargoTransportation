from django import forms

from .models import Clients, Cargo, Orders


class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name_client', 'number_telephone', 'email']
        widgets = {
            'name_client': forms.TextInput(attrs={'placeholder': "Имя"}),
            'number_telephone': forms.TextInput(attrs={'type': 'tel', 'placeholder': "Телефон"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"})
        }


class CargoInfoForm1(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name_order']
        widgets = {
            'name_order': forms.TextInput(attrs={'placeholder': "Название груза"})
        }


#
#
class CargoInfoForm2(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['type', 'weight']
        widgets = {
            'type': forms.TextInput(attrs={'placeholder': "Тип груза"}),
            'weight': forms.TextInput(attrs={'placeholder': "Вес груза"})
        }


class CargoInfoForm3(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['dimensions', 'type_transportation']
        widgets = {
            'dimensions': forms.TextInput(attrs={'placeholder': "Габариты груза"}),
            'type_transportation': forms.TextInput(attrs={'placeholder': "Тип перевозки"})
        }


class RouteInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['point_departure', 'point_destination', 'period_execution']
        widgets = {
            'point_departure': forms.TextInput(attrs={'placeholder': "Точка отправки"}),
            'point_destination': forms.TextInput(attrs={'placeholder': "Точка доставки"}),
            'period_execution': forms.TextInput(attrs={'placeholder': "Срок выполнения"})
        }


class PriceInfoForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['price_order']
        widgets = {
            'price_order': forms.TextInput(attrs={'disabled': True, 'values': '0р.'})
        }
