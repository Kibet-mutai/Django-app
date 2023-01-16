from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    images = models.ImageField(upload_to='static/images')

    def __str__(self):
        return f'{self.name}'
