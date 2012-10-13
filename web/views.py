from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, DetailView

from web.models import Trip, Item, TripItemRelationship, Text, TripUserRelationship
from django.db.models import Count
from social_auth.models import UserSocialAuth
from pprint import pprint
import facebook
import json


from web.forms import TripForm

class StartView( TemplateView):
	def get_context_data(self, **kwargs ):
		context = super(StartView, self).get_context_data(**kwargs)
		texts = dict(((text.key, text.content) for text in Text.objects.filter( page__key = 'start' )))
		context['texts'] = texts
		return context
		
class LogoutView( TemplateView):
	def get_context_data(self, **kwargs ):
		context = super(StartView, self).get_context_data(**kwargs)
		context['texts'] = dict(((text.key, text.content) for text in Text.objects.filter( page__key = 'logout' )))
		return context
		

class TripCreateView(CreateView):
 	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.owner = self.request.user
		trips_of_type = Trip.objects.filter( type_of_trip = obj.type_of_trip)
		items = Item.objects.filter(trip__in=trips_of_type).distinct()[:10]
		obj.save()
	
		tripUserRelationsship = TripUserRelationship( trip = obj, user = self.request.user )
		tripUserRelationsship.owner = True
		tripUserRelationsship.save()
		
		for item in items:
			r1 = TripItemRelationship(trip = obj, item = item )
			r1.owner = self.request.user
			r1.quantity = 1
			r1.save()
		return HttpResponseRedirect('/web/trip/'+str(obj.id))

class TripDetailView(DetailView):
	def get_context_data(self, **kwargs):
		queryset = UserSocialAuth.objects.filter(provider='facebook', user = self.request.user )
		if queryset :
			instance = queryset.get()
			graph = facebook.GraphAPI(instance.tokens['access_token'])
			profile = graph.get_object("me")
			friends = graph.get_connections("me", "friends")['data']
			friendsId = [x['id'] for x in friends]
			pprint( "All Facebook Friends ")
			pprint(friendsId)
			friends_on_packmythings = UserSocialAuth.objects.filter(provider = 'facebook', uid__in=friendsId )
			pprint("Friends on Pack My Things ")
			pprint(friends_on_packmythings )

		tripMembers =  TripUserRelationship.objects.filter( trip = self.object, user = self.request.user)
		context = super(TripDetailView, self).get_context_data(**kwargs)
		trips_of_type = Trip.objects.filter( type_of_trip = self.object.type_of_trip)
		context['items'] = TripItemRelationship.objects.filter(trip=self.object, owner=self.request.user).distinct()
		context['all_items'] = Item.objects.all().exclude( trip = self.object )
		context['popular_items'] = Item.objects.filter(trip__in = trips_of_type).exclude( trip = self.object).annotate(num_trips=Count('trip')).order_by('-num_trips')
		context['texts'] = dict(((text.key, text.content) for text in Text.objects.filter( page__key = 'trip/detail' )))
		if len(tripMembers ) > 0 :
			context['is_owner'] = tripMembers[0].owner
		return context

    
