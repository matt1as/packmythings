from django.db import models
from django.contrib.auth.models import User, Group
from registration.signals import user_activated
from social_auth.signals import socialauth_registered
from social_auth.backends.facebook import FacebookBackend
from cms.models import CMSPlugin
from django.utils.functional import SimpleLazyObject


	
class Item(models.Model):
  name = models.CharField(max_length=200 )
  def __unicode__(self):
    return self.name
 
class TypeOfTrip(models.Model):
	name = models.CharField('Name of the trip', max_length=200)
	items = models.ManyToManyField( Item, null=True, blank=True, verbose_name='List of Items', through='ItemTypeOfTripRelationship')
  
	def __unicode__(self):
		return self.name

class Trip(models.Model):
  name = models.CharField('Name of the trip', max_length=200)
# owner = models.ForeignKey(User)
  destination = models.CharField( max_length=200, null=True)
  startDate = models.DateField('Start Date of the Trip')
  endDate = models.DateField('End Date of the Trip')
#  length = models.IntegerField('Length in days')
  type_of_trip = models.ForeignKey(TypeOfTrip)
  members = models.ManyToManyField( User, through='TripUserRelationship', null=True, blank=True)
  items = models.ManyToManyField( Item, through='TripItemRelationship', null=True, blank=True)
  description = models.TextField('Describe your trip', max_length=400 )
  def __unicode__(self):
    return self.name

class TripItemRelationship(models.Model):
		item = models.ForeignKey(Item)
		trip = models.ForeignKey( Trip )
		quantity = models.IntegerField('Quantity', default=1)
		packed = models.BooleanField('Is the item packed')
		owner = models.ForeignKey( User )
		def __unicode__(self):
			return self.trip.name + " - " + self.item.name
			
class TripUserRelationship(models.Model):
	user = models.ForeignKey(User)
	trip = models.ForeignKey( Trip )
	owner = models.BooleanField()
	def __unicode__(self):
		return self.trip.name + " - " + self.user.username


class ItemTypeOfTripRelationship(models.Model):
	counter = models.IntegerField()
	item = models.ForeignKey(Item)
	owner = models.ForeignKey(User)
	type_of_trip = models.ForeignKey( TypeOfTrip )

class Page(models.Model):
	key = models.CharField('Name', max_length = 200 )
	def __unicode__(self):
		return self.key	

class Text(models.Model):
	key = models.CharField('Name', max_length=200 )
	content = models.TextField('Text', max_length=800 )
	page = models.ForeignKey( Page )
	def __unicode__(self):
		return self.key



# Register signals, this is done in models.py to make sure they're registered early in the app life cycle
def new_user_activated(sender, user, request, **kwarg):
	g = Group.objects.get(name='Member') 
	g.user_set.add(user)
	
def new_social_users_handler(sender, user, response, details, **kwargs):
	g = Group.objects.get(name='Member') 
	g.user_set.add(user)

user_activated.connect(new_user_activated)
socialauth_registered.connect(new_social_users_handler, sender = None )

# Create CMS Plugins
class ItemListPlugin(CMSPlugin):
	trip = models.ForeignKey(Trip)
	

class IterableLazyObject(SimpleLazyObject):
	def __iter__(self):
		if self._wrapped is None: self._setup()
		return self._wrapped.__iter__()

