from django.db import models
from . import utility
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = PhoneNumberField()
    status = models.CharField(max_length=8, choices=utility.status_choice)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = PhoneNumberField()
    status = models.CharField(max_length=8, choices=utility.status_choice)
    created_at = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
       return self.name


