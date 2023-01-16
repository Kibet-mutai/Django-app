from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

api_view(['GET'])
def Users(request):
    if request.method == 'GET':
        message = [{'message':'Welcome!'}]
        return JsonResponse(message, safe=False)