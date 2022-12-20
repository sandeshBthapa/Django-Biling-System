from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscription, name='all_sub'),
    path('create/', views.create_subscription, name='create-subscription'),
    path("delete/<str:pk>/", views.delete_subscription, name="delete-subscription"),
    path("update/<str:pk>/", views.update_subscription, name="update-subscription"),

]