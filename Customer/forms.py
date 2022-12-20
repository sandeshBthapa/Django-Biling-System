from django.forms import ModelForm
from .models import Customer
from django import forms

class CustomerModelForm(ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'Enter your name'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'enter phone number'}))
    class Meta:
        model = Customer
        fields = '__all__'