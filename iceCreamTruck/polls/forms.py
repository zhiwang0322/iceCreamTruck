from django import forms
from .models import OrderForm
from .models import ProductForm
class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = '__all__'
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = '__all__'