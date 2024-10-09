from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import RegistrationSerializer


User = get_user_model()
class RegisterAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

