from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class TripsHook(CMSApp):
	name = _("Trips")
	urls = ["web.urls"]

class ApiHook(CMSApp):
	name = _("Api")
	urls = ["web.urls"]
	
apphook_pool.register(TripsHook)
apphook_pool.register(ApiHook)
