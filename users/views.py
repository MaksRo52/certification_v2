from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsAdmin, IsUser
from users.serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)  # Allow unauthenticated users to create accounts

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin]


class UserUpdateApiView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdmin | IsUser]


class UserDestroyApiView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdmin]
