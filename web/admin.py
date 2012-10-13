from django.contrib import admin
from web.models import *
from tinymce import *

# we define our resources to add to admin pages
class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/scripts/editor.js',
  )
  css = {
    'all': ('/static/css/editor.css',),
  }


class TextAdmin(admin.ModelAdmin):
	list_filter = ('page','key')
	Media = CommonMedia

admin.site.register(TypeOfTrip)
admin.site.register(Page)
admin.site.register(Text, TextAdmin )
admin.site.register(TripItemRelationship)
admin.site.register(TripUserRelationship)