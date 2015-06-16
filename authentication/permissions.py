from rest_framework import permissions

# Account Owner Permissions 

class IsAccountOwner(permissions, BasePermissions):
	def has_object_permissions(self, request, view, account):
		if request.user:
			return account == request.user
			
		return False