from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomIsAuthenticatedOrReadOnly(BasePermission):
    # flow --> has_perm --> has_obj_perm
    message = "hello world"

    def has_permission(self, request, view):  # level permission
        user = request.user
        method = request.method
        print("METHOD ", method)
        if not user.is_authenticated:
            if method not in SAFE_METHODS:
                return False

            return True

        return True  # returning True if user is authenticated

    def has_object_permission(self, request, view, obj):  # object level permission
        ## has object permission by default returns True for GET request
        user = request.user
        print("Blog's(OBJECT) User --> ", obj.user)
        print("Current User --> ", user)
        print("METHOD2 ", request.method)
        if request.user == obj.user:
            return True

        return False



class CustomIsAdminOrReadOnly(BasePermission):
    pass

