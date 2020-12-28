from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions to allow only the owners of the object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are allowed to only the owner of the Post
        return obj.owner == request.user
