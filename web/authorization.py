from tastypie.authorization import DjangoAuthorization

class OwnerAuthorization(DjangoAuthorization):

	def apply_limits(self, request, object_list):
		if request and hasattr(request, 'user'):
			if request.user.is_authenticated():
				object_list = object_list.filter(owner=request.user)
			else:
				object_list = object_list.none()

			return object_list