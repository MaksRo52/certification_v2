from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny, IsAuthenticated

from main.models import Commentary, Post
from main.serializers import CommentarySerializer, PostSerializer
from users.permissions import IsAdmin, IsOwner

# Вьюсет для постов


class PostCreateApiView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostListApiView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostRetrieveApiView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateApiView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class PostDestroyApiView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


# Вьюсет для комментариев
class CommentaryCreateApiView(CreateAPIView):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(owner=self.request.user, post=post)


class CommentaryListApiView(ListAPIView):
    serializer_class = CommentarySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Commentary.objects.filter(post_id=self.kwargs["post_id"])


class CommentaryRetrieveApiView(RetrieveAPIView):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()
    permission_classes = [AllowAny]


class CommentaryUpdateApiView(UpdateAPIView):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class CommentaryDestroyApiView(DestroyAPIView):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
