from rest_framework import permissions


class IsAuthenticatedOrAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

class IsReviewAuthorOrReadonly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author ==  request.user
        

"""
# it returns the requested method in safe_methods or if it a is_admin
#SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

IsAdminUser - Allows access only to admin users.(request.user and request.user.is_staff
"""
