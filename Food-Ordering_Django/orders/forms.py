from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number')
    expiration_date = forms.CharField(label='Expiration Date')
    cvv = forms.CharField(label='CVV')
    cardholder_name = forms.CharField(label='Cardholder Name')
