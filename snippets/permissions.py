from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not obj.owner:
            raise NotImplementedError(
                "Only use this permission w/ object with a 'owner' field")

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user == obj.owner:
            return True

        return False
