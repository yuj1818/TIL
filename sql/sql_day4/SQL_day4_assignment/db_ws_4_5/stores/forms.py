from django import forms
from .models import Store, Product

class StoreForm(forms.ModelForm):
    is_franchise = forms.BooleanField(
        required=False
    )
    address = forms.CharField(
        widget=forms.TextInput()
    )
    class Meta:
        model = Store
        fields = '__all__'

class ProductForm(forms.ModelForm):
    adult = forms.BooleanField(
        required=False
    )
    name = forms.CharField(
        widget=forms.TextInput()
    )
    class Meta:
        model = Product
        exclude = ('store', 'user',)