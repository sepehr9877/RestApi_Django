
from rest_framework import permissions
from rest_framework.authtoken.models import Token


class AccountPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method ==permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id


