from rest_framework import serializers

from .models import Commentary, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "picture"]


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ["id", "content", "owner"]
