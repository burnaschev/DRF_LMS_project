from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        else:
            return request.method in permissions.SAFE_METHODS

