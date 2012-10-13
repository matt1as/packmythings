from django.views.generic import DetailView, View, ListView, CreateView, UpdateView, TemplateView
from web.models import Trip, TripUserRelationship, IterableLazyObject

class BaseTemplateView( TemplateView ):
	def get_context_data(self, **kwargs):
		context = super(BaseTemplateView, self).get_context_data(**kwargs)
		
#		if self.request.user.is_authenticated():
#			if trip.objects :
#				context['my_trips'] = Trip.objects.filter( self.request.user in self.object.members )[:10]
		return context

class BaseListView( ListView ):
	def get_context_data(self, **kwargs):
		context = super(BaseListView, self).get_context_data(**kwargs)
		
#		if self.request.user.is_authenticated():
#			context['my_trips'] = Trip.objects.filter(  self.request.user in self.object.members  )[:10]
		return context

class BaseDetailView(DetailView):
  def get_context_data(self, **kwargs):
	context = super(DetailView, self).get_context_data(**kwargs)
#	if self.request.user.is_authenticated():
#		context['my_trips'] = Trip.objects.filter( self.request.user in self.object.members )[:10]	
	return context    

class BaseCreateView(CreateView):
	def get_context_data(self, **kwargs):
		context = super(BaseCreateView, self).get_context_data(**kwargs)
#		if self.request.user.is_authenticated():
#			context['my_trips'] =  Trip.objects.filter( members__in = self.request.user )
		return context
		
class BaseUpdateView(UpdateView):
	def get_context_data(self, **kwargs):
		context = super(BaseUpdateView, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated():
			context['my_trips'] = Trip.objects.filter( self.request.user in self.object.members )[:10]
#			context['top_bags'] = Bag.objects.all()[:10]
			return context