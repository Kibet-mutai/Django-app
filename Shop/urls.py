from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('products', views.Products),
    path('products/<int:id>', views.products_detail),
    path('products/create', views.create_product),
    path('products/admin/<int:id>', views.detail_view)
]