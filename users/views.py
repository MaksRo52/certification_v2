from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, \
    UpdateAPIView, DestroyAPIView

from users.serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieveApiView(RetrieveAPIView):
    serializer_class = UserSerializer

class UserUpdateApiView(UpdateAPIView):
    serializer_class = UserSerializer

class UserDestroyApiView(DestroyAPIView):
    serializer_class = UserSerializer
