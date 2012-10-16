from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, RedirectView, FormView, TemplateView

from web.api import UserResource, TripResource, ItemResource, TypeOfTripResource, TripItemRelationshipResource, PopularItemResource
from web.sitemap import TripSitemap
from tastypie.api import Api
from django.views.generic.simple import direct_to_template, redirect_to

from cms.sitemaps import CMSSitemap

import allauth
import social_auth




#-------------- Admin ----------------------
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    
	(r'^start/$', redirect_to, {'url': '/web/start/'}),

#------------ Registration views --------
	(r'^accounts/', include('registration.backends.default.urls')),


#------------ Admin Views  --------------
    url(r'^admin/', include(admin.site.urls)),

#---------- Social Login --------------
	url(r'', include('social_auth.urls')),
	
#---------- CMS -----------------------
	url(r'^', include('cms.urls')),
	
#--------- SITEMAP --------------------
	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap, 'trips': TripSitemap} }),
)
