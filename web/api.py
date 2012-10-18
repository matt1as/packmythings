# myapp/api.py
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.constants import ALL
from tastypie.authorization import DjangoAuthorization,Authorization
from tastypie import fields
from web.models import *
from web.authorization import *
from django.contrib.auth.models import User
from django.db.models import Count



class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()

class ItemResource(ModelResource):
	class Meta:
		queryset = Item.objects.all()
		authorization = Authorization()
		filtering = { 
	  		'name': ALL, 
		}
		
	def obj_create(self, bundle, request, **kwargs):
		item = Item.objects.filter( name = bundle.data['name'] ).distinct()
		print item
		if( not item )  :
			print "Creating object"
			return super(ItemResource, self).obj_create(bundle, request, owner=request.user)
		else:
			print "Not creating object"
			return item[0]
		
class PopularItemResource(ModelResource):
	class Meta:
		queryset = TypeOfTrip.objects.filter().annotate(num_trips=Count('trip')).order_by('-num_trips')
		authorization = DjangoAuthorization()
		filtering = { 
			'type_of_trip': ALL, 
		}
		
		def dehydrate_name(self, bundle):
			bundle.data['items'] = self.items
			return bundle
			

class TypeOfTripResource(ModelResource):
	class Meta:
		queryset = TypeOfTrip.objects.all()
           
class TripResource(ModelResource):
	item  = fields.ToManyField( ItemResource, 'items', full=True )
	#owner = fields.ForeignKey( UserResource, 'owner' )
	type_of_trip = fields.ForeignKey( TypeOfTripResource, 'type_of_trip' )
		
	class Meta:
		queryset = Trip.objects.all()
		authorization = DjangoAuthorization()
		filtering = { 
			'name': ALL,
			#'owner': ALL,
			'length': ALL,
			'type_of_trip': ALL,
	}
	

#	def obj_create(self, bundle, request=None, **kwargs):#
#		typeOfTripRelationship = ItemTypeOfTripRelationsship.objects.filter(	typeOfTrip = self.type_of_trip)		
#		return super(TripResource, self).obj_create(bundle, request)

class TripUserRelationshipResource(ModelResource):
	class Meta:
		queryset = TripUserRelationship.objects.all()
		

class TripItemRelationshipResource(ModelResource):
	item  = fields.ForeignKey( ItemResource, 'item' )
	trip = fields.ForeignKey( TripResource, 'trip')
	owner = fields.ForeignKey( UserResource, 'owner' )

  # Attach the user on creation
	def obj_create(self, bundle, request, **kwargs):
		return super(TripItemRelationshipResource, self).obj_create(bundle, request, owner=request.user)

#	def hydrate_owner(self, bundle):
#		bundle.data['owner'] =  '/api/v1/user/' + self.request.user
#		return bundle
	class Meta:
		authorization = Authorization()
		queryset = TripItemRelationship.objects.all()
	
	def apply_authorization_limits(self, request, object_list):
		if object_list._result_cache is not None:
			self._pre_limits = len(object_list._result_cache)
		else:
			self._pre_limits = 0
			# Just to demonstrate the per-resource hooks.
			new_object_list = super(TripItemRelationshipResource, self).apply_authorization_limits(request, object_list)
		if object_list._result_cache is not None:
			self._post_limits = len(object_list._result_cache)
		else:
			self._post_limits = 0
			return new_object_list
