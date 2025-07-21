# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .token import MyTokenObtainPairSerializer
from .serializers import RegistarSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegistarView(generics.CreateAPIView):
    serializer_class = RegistarSerializer
    permission_classes = [AllowAny]