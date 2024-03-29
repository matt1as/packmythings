# Django settings for packmythings project.
# Please make local changes to local_settings.py
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
	'cms.context_processors.media',
	'sekizai.context_processors.sekizai',
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = ''

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Stockholm'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-lr3j!+497r(dj)*ar^17u+qc44^vtg7otv6q65b6xjg%i=@y#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
 	'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
	'web.middleware.MyTrips'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



ROOT_URLCONF = 'packmythings.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'packmythings.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like '/home/html/django_templates' or 'C:/www/django/templates'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'south',
	'web',
	'django.contrib.admin',
#    'django.contrib.admindocs',
	'social_auth',
	'cms',
	'menus',
	'mptt',
	'cms.plugins.text',
#	'cms.plugins.picture',
	'cms.plugins.link',
#	'cms.plugins.file',
	'cms.plugins.snippet',
	'cms.plugins.googlemap',
	'sekizai',
	'cmsplugin_contact',
	'filer',
	'easy_thumbnails',
	'disqus',
	'google_analytics',
	'django.contrib.sitemaps',
	'cmsplugin_filer_file',
	'cmsplugin_filer_folder',
	'cmsplugin_filer_image',
	'cmsplugin_filer_teaser',
#	'cmsplugin_filer_video',
)

GOOGLE_ANALYTICS_MODEL = True

DISQUS_API_KEY = 't2uDPsvHxJrTqhX12a4lnynPbPjOSlGS6P2EuMOM72V2mjrlRGvEW8hQUwZCSFc6'
DISQUS_WEBSITE_SHORTNAME = 'packmythings'

LOGIN_REDIRECT_URL = '/'

LOGOUT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 10

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend', 
	'social_auth.backends.facebook.FacebookBackend', 
	'social_auth.backends.twitter.TwitterBackend', 
	'social_auth.backends.google.GoogleBackend'  )

TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/tiny_mce'

# -------- Facebook settings 
FACEBOOK_APP_ID              = '386252088095260'
FACEBOOK_API_SECRET          = '1435c035c0b9a089427fe61719636823'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']


# --------- Google settings
GOOGLE_OAUTH2_CLIENT_ID = '667492745451.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'lqYZhhakfx8vQ6ZIhNJZ6Bi7'

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/login/'


SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

CMS_TEMPLATES = (
    ('main_cms.html', 'Main page with one column'),
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

try:
    from local_settings import *
except:
    pass