from rest_framework import permissions

from users.models import UserRoles


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            if request.method == 'POST':
                return False
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MEMBER:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.users == request.user
