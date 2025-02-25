from rest_framework import serializers
from .models import Post, Commentary

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ['post', 'text', 'author']