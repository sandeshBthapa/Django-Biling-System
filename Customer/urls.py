from django.urls import path
from . import views
urlpatterns = [

    path('',views.customer_list, name='list_customer'),
    path('create',views.customer_create_form, name='create_customer'),
    path("delete/<str:pk>/", views.delete_customer, name="delete-customer"),
    path("update/<str:pk>/", views.update_customer, name="update-customer"),

    path('signup/', views.signup_page, name='sign_up'),
    path('signin/', views.signin_page, name='sign_in'),
    path("logout", views.logOutPage, name="logout"),



]