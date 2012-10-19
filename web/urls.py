from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from web.api import UserResource, TripResource, ItemResource, TypeOfTripResource, TripItemRelationshipResource, TripUserRelationshipResource, PopularItemResource
from tastypie.api import Api
from django.contrib.auth.decorators import login_required


#--------------- Models and views--------------------
from web.models import Trip, Item
from web.forms import TripForm, ItemForm, UserForm
from web.views import TripDetailView, TripCreateView, StartView
#from web.base_views import BaseUpdateView, BaseTemplateView


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(TripResource())
v1_api.register(ItemResource())
v1_api.register(TypeOfTripResource())
v1_api.register(TripItemRelationshipResource())
v1_api.register(TripUserRelationshipResource())
v1_api.register(PopularItemResource())

urlpatterns = patterns('',
    
#	(r'^$', RedirectView.as_view(
#		url = 'web/start'
#	)),
	
	(r'^tinymce/', include('tinymce.urls')),
	
	(r'^start/$', StartView.as_view( template_name = 'start.html')),
	
#------------ Robots.txt ---------------
    (r'^robots\.txt$', direct_to_template,
      {'template': 'robots.txt', 'mimetype': 'text/plain'}),
#------------ Trip Views  --------------
    (r'^trip/(?P<pk>\d+)/$', TripDetailView.as_view(
        model=Trip,
        template_name='trip/detail.html'
    ),'','detail_trip'),
  
    (r'^trip/$', ListView.as_view(
		model=Trip,
		template_name='trip/list.html'
      
    )),
    
	(r'^trip/create/$', login_required(TripCreateView.as_view(
	  	form_class=TripForm,
        template_name='trip/create.html',
		success_url='/web/trip/'
    ))),
	
#------------ Item Views  --------------
    (r'^item/$', ListView.as_view(
        model=Item,
        template_name='item/list.html'
    )),

    (r'^item/(?P<pk>\d+)/$',DetailView.as_view(
        model=Item,
        template_name='item/detail.html',
    )),
	(r'^item/create/$', login_required(CreateView.as_view(
	  	form_class=ItemForm,
        template_name='item/create.html',
		success_url='/'
    ))),


#------------ Api Views  -------------- 
	(r'^', include(v1_api.urls)),
)