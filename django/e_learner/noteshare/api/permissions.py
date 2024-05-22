from rest_framework import permissions
from .models import Resource

class HasPostedResource(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            # Allow posting resources
            if view.action == 'create':
                return True
            # Check if the user has posted at least one resource
            return Resource.objects.filter(user=request.user).exists()
        return False
