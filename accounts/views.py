from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer



class UserRegistration(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer