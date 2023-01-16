from django.db import models
from Shop.models import product
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class CartItem(models.Model):
    products = models.ManyToManyField(product)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # price = models.DecimalField(max_digits=100, decimal_places=2, null=True)