from django.forms import ModelForm
from .models import Subscription
from django import forms
class SubscriptionCreateForm(ModelForm):
    to_date = forms.CharField(widget= forms.DateInput(attrs={'placeholder':'Enter in YYYY-MM-DD'}))
    class Meta:
        model = Subscription
        fields =['customer_name', 'to_date', 'amount', 'status']