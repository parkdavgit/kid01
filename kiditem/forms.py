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
        fields = ['street_address', 'apartment_address', 'country', 'zip', 'address_type']
        widgets = {
            'street_address': forms.TextInput(attrs={'readonly': 'readonly'}),
            'apartment_address': forms.TextInput(),
            'country': forms.CountryField(multiple=False),
            'zip': forms.TextInput(),
            'address_type': forms.TextInput(),
        }







    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
