from rest_framework.permissions import BasePermission


class IsSuperUserPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser and request.user.is_staff)