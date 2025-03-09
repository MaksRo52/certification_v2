from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter

from main.apps import MainConfig
from main.views import (CommentaryCreateApiView, CommentaryDestroyApiView,
                        CommentaryListApiView, CommentaryRetrieveApiView,
                        CommentaryUpdateApiView, PostCreateApiView,
                        PostDestroyApiView, PostListApiView,
                        PostRetrieveApiView, PostUpdateApiView)

app_name = MainConfig.name


urlpatterns = [
    # URL для постов
    path("", PostListApiView.as_view(), name="post_list"),
    path("create/", PostCreateApiView.as_view(), name="post_create"),
    path("<int:pk>/", PostRetrieveApiView.as_view(), name="post_detail"),
    path("<int:pk>/update/", PostUpdateApiView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDestroyApiView.as_view(), name="post_delete"),
    # URL для комментариев
    path(
        "<int:post_id>/comments/", CommentaryListApiView.as_view(), name="comment_list"
    ),
    path(
        "<int:post_id>/comments/create/",
        CommentaryCreateApiView.as_view(),
        name="comment_create",
    ),
    path(
        "<int:post_id>/comments/<int:pk>/",
        CommentaryRetrieveApiView.as_view(),
        name="comment_detail",
    ),
    path(
        "<int:post_id>/comments/<int:pk>/update/",
        CommentaryUpdateApiView.as_view(),
        name="comment_update",
    ),
    path(
        "<int:post_id>/comments/<int:pk>/delete/",
        CommentaryDestroyApiView.as_view(),
        name="comment_delete",
    ),
]
