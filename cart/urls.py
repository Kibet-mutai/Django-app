from django.urls import path
from . import views

urlpatterns = [
    path('add_cart', views.add_to_cart),
    path('view_cart', views.cart_items)
]