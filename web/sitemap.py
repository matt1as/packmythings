from django.contrib.sitemaps import Sitemap
from web.models import Trip

class TripSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Trip.objects.all()
   
    def location( self, obj):
      return '/web/trip/' + str( obj.id )