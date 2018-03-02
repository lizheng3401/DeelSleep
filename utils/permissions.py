from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminOrUpdateSelf(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser == 1

    def has_object_permission(self, request, view, obj):
        if request.method == "Post":
            return request.user == obj