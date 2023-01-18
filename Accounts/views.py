from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from Accounts.serializers import RegisterSerializer, TokenSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
User = get_user_model()

api_view(['GET'])
def Users(request):
    if request.method == 'GET':
        message = [{'message':'Welcome!'}]
        return JsonResponse(message, safe=False)



class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully."
        })

class TokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer