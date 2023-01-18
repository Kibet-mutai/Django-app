from rest_framework import serializers
from cart.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields = '__all__'