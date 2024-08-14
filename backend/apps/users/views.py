from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.users.serializer import UserSerializer

# Create your views here.
UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


    