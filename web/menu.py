from menus.base import Menu, NavigationNode
from cms.menu_bases import CMSAttachMenu
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from models import Trip

class TripMenu(CMSAttachMenu):
	
	name = _("Trips Menu")
	
	def get_nodes(self, request):
		nodes = []
		#if request.user.is_authenticated():
			#my_trips= Trip.objects.filter( request.user in self.members )
			#for index, trip in 	enumerate( my_trips ):
			#	n = NavigationNode(_(trip.name), '/web/trip/' + str(trip.id), index )
			#	nodes.append( n )
		return nodes

menu_pool.register_menu(TripMenu)