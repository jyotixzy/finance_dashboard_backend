from rest_framework.permissions import BasePermission

class RoleBasedPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # agar user login nahi hai
        if not user.is_authenticated:
            return False

        # GET request → sab roles allowed
        if request.method in ['GET']:
            return True

        # Viewer → sirf read
        if user.role == 'viewer':
            return False

        # Analyst → read only (no create/update/delete)
        if user.role == 'analyst':
            return False

        # Admin → full access
        if user.role == 'admin':
            return True

        return False