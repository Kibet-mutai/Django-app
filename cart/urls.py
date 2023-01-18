from django.urls import path
from . import views



urlpatterns = [
    path('view_cart', views.cart_items),
    path('add_cart', views.add_to_cart),
    path('cart_detail/<int:id>', views.cart_detail)
]