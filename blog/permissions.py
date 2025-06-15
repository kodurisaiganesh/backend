# blog/permissions.py

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a blog to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods: GET, HEAD, OPTIONS — always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only if user is the author
        return obj.author == request.user
