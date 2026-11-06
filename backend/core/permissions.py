from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

class BaseRBACPermission(BasePermission):
    pass

class IsAdminUser(BaseRBACPermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_authenticated:
            return getattr(request.user, 'role', None) == 'ADMIN' == 'ADMIN'
        else:
            return False
    
class HasClearanceLevel(BaseRBACPermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.user.is_authenticated:
            required_clearance_level = getattr(view, 'required_clearance_level', 1)
            return required_clearance_level <= getattr(request.user, 'clearance_level', 0)

        else:
            return False