# shop/forms.py
from django import forms

class CartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1)

class SubmitCartForm(forms.Form):
    email = forms.EmailField()
