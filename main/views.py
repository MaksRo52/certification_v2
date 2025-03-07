from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)

from main.models import Commentary
from main.serializers import CommentarySerializer, PostSerializer

# Вьюсет для постов

class PostCreateApiView(CreateAPIView):
    serializer_class = PostSerializer

class PostRetrieveApiView(RetrieveAPIView):
    serializer_class = PostSerializer

class PostUpdateApiView(UpdateAPIView):
    serializer_class = PostSerializer

class PostDestroyApiView(DestroyAPIView):
    serializer_class = PostSerializer

# Вьюсет для комментариев
class CommentaryCreateApiView(CreateAPIView):
    serializer_class = CommentarySerializer

class CommentaryRetrieveApiView(RetrieveAPIView):
    serializer_class = CommentarySerializer

class CommentaryUpdateApiView(UpdateAPIView):
    serializer_class = CommentarySerializer

class CommentaryDestroyApiView(DestroyAPIView):
    serializer_class = CommentarySerializer