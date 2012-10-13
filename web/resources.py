from djangorestframework.resources import ModelResource
from web.models import Item, Trip, TripItemRelationship

class ItemResource(ModelResource):
    model = Item

class TripResource(ModelResource):
    model = Trip

class TripItemRelationshipResource(ModelResource):
    model = TripItemRelationship