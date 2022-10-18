import re
from urllib import request
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.method in permissions.SAFE_METHODS else bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else obj.user == request.user