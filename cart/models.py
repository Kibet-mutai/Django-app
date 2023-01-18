from django.db import models
from Shop.models import product
from django.contrib.auth import get_user_model
from decimal import Decimal


User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    products = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    quantities = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))



    def __str__(self):
        return f'{self.user}'

