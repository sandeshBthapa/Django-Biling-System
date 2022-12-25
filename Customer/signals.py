from .models import Customer
from django.db.models.signals import post_save, post_delete



def create_customer(sender, instance, created, **kwargs):
    if created:
        user = instance
        customer = Customer.objects.create(
            name=user.first_name,
            email=user.email,
            phone = user.phone,
            status = user.status,
            created_at = user.date_joined

        )


# def updateUser(sender, instance, created, **kwargs):
#     customer = instance
#     user = customer.user
#     if created == False:
#         user.username = customer.username
#         user.email = customer.email
#         user.phone = customer.phone
#         user.status = customer.status
#         user.save()


# def delete_profile(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()


from django.contrib.auth import get_user_model
User = get_user_model()

post_save.connect(create_customer, sender=User)
# post_save.connect(updateUser, sender=Customer)
# post_delete.connect(delete_profile, sender=Customer)
