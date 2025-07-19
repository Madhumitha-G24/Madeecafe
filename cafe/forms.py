from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name', 'email', 'message',
            'espresso', 'latte', 'cappuccino',
            'brownie', 'croissant', 'iced_mocha'
        ]
