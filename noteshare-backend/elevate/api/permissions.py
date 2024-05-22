# api/permissions.py

from rest_framework.permissions import BasePermission

class HasPostedResource(BasePermission):
    """
    Custom permission to only allow users who have posted at least one resource to access the resource list.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Check if the user has posted at least one resource
            return request.user.resource_set.exists()
        return False
