from django.forms import ModelForm
from .models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomerModelForm(ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'Enter your name'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'enter phone number'}))
    class Meta:
        model = Customer
        fields = '__all__'

class UserCreationModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','phone','status','email','password1']
