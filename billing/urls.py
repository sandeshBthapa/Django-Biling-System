
from django.contrib import admin
from django.urls import path,include
from Customer.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main-page'),
    path('customer/',include('Customer.urls')),
    path('subscription/',include('Subscription.urls')),

]
