"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, formset_factory
from django.forms.models import modelformset_factory
from .models import Order, Order_item


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'order_contact_name', 'order_contact_phone']

class ItemOrderForm(forms.ModelForm):
    class Meta:
        model = Order_item
        fields = ['item_sku', 'item_descr', 'item_vendor', 'item_qty', 'item_paid']


   