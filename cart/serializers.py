from rest_framework import serializers
from cart.models import Cart, CartItem


class Cartserializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
