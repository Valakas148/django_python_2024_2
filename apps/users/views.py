from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from apps.users.serializer import UserSerializer

# Create your views here.
UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


    