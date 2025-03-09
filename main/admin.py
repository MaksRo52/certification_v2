from django.contrib import admin
from django.urls import reverse

from main.models import Commentary, Post
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner_link", "created_at")
    list_filter = ("created_at",)

    def owner_link(self, obj):
        if obj.owner:
            admin_url = reverse('admin:users_user_change', args=[obj.owner.id])
            return admin.utils.format_html(f'<a href="{admin_url}">{obj.owner}</a>')
        return "Автора нет"


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("post", "owner", "content", "created_at")
