from django.db import models
from . import utility
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    status = models.CharField(max_length=8, choices=utility.status_choice)
    created_at = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
       return self.name
