from web.models import Trip, TripUserRelationship

class MyTrips:
	def process_request(self, request):
		if request.user.is_authenticated():
			request.my_trips = TripUserRelationship.objects.filter( user = request.user ).all()
		return None