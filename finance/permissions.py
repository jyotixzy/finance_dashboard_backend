from rest_framework.permissions import BasePermission

class RoleBasedPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

     
        if request.method in ['GET']:
            return True

      
        if user.role == 'viewer':
            return False


        if user.role == 'analyst':
            return False

     
        if user.role == 'admin':
            return True

        return False
