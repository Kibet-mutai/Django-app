from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from cart.serializers import OrdersSerializer
from cart.models import Order
from Shop.models import product
from rest_framework import viewsets, permissions


# Create your views here.

@api_view(['GET'])
def cart_items(request):
    items = Order.objects.all()
    serializer = OrdersSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product_cart = product.objects.get(id=product_id)
    Order(user=user, product=product_cart).save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])

def cart_detail(request, id):
    try:
        cart_items = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrdersSerializer(cart_items)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

