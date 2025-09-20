# api/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow authenticated users to read (GET/HEAD/OPTIONS).
    Allow only staff (is_staff) users to create, update, or delete.
    Unauthenticated users are not allowed.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users to make safe (read) requests
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        # For non-safe methods (POST, PUT, PATCH, DELETE), allow only staff users
        return bool(request.user and request.user.is_staff)
