from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from cart.serializers import CartItemSerializer, Cartserializer
from cart.models import Cart, CartItem

# Create your views here.

@api_view(['GET'])
def cart_items(request):
    items = CartItem.objects.all()
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    serializer = CartItemSerializer(many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
