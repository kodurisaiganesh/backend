# blog/permissions.py

from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the author of a blog post to edit or delete it.
    """

    def has_permission(self, request, view):
        # Always allow authenticated users for safe methods, else check object-level
        return True

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write permissions only to the blog's author
        return obj.author == request.user
