from django import forms
from .models import Order, Address


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'amount', 'quantity']
        fields = ['quantity']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'amount': forms.TextInput(),
            'quantity': forms.TextInput(),

           
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street']
       
        widgets = {
            'street': forms.TextInput(),
                       
        }
