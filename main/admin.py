from django.contrib import admin

from main.models import Commentary, Post
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone_number")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "owner", "content", "created_at")
