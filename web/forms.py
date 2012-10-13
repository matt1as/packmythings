from django.forms import ModelForm, DateField
from web.models import Trip, Item
from django.contrib.auth.models import User
from django.db import models


def make_custom_datefield(f):
	formfield = f.formfield()
	if isinstance(f, models.DateField):
		formfield.widget.format = '%m/%d/%Y'
		formfield.widget.attrs.update({'class':'datePicker'})
	return formfield
		
# Create the form class.
class TripForm(ModelForm):
	formfield_callback = make_custom_datefield
    	
	class Meta:
		model = Trip
		exclude = ('items', 'owner')		
		

#Create the form class.
class ItemForm(ModelForm):
	class Meta:
		model = Item
		
class UserForm(ModelForm):
	class Meta:
		model = User
		
