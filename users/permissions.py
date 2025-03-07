from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
        Проверка на права Админа.
        """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="admins").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверка на автора.
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

class IsUser(permissions.BasePermission):
    """
    Проверка на владельца.
    """
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False