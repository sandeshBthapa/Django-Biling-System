from django.db import models
from Customer.models import Customer
from . import utility

# Create your models here.

class Subscription(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField()
    amount = models.FloatField()
    status = models.CharField(max_length=6, choices=utility.status_choices)

    def __str__(self):
        return self.customer_name.name