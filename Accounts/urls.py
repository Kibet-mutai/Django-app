from django.urls import path
from . import views
from Accounts.views import Register, TokenView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth', views.Users),
    path('register', Register.as_view()),
    path('login/', TokenView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
]