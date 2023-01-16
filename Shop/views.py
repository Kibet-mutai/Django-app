from Shop.models import product
from Shop.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

# Create your views here.

@api_view(['GET'])
def Index(request):
    if request.method == 'GET':
        message = [{'message':'Welcome!'}]
        return JsonResponse(message, safe=False)



@api_view(['GET'])
def Products(request):
    items = product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def products_detail(request, id):
    try:
        items = product.objects.get(id=id)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE', 'POST'])
def detail_view(request,id):
    try:
        products = product.objects.get(id=id)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(serializer.data)
       
    elif request.method == 'PUT':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)