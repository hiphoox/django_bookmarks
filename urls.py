from django.conf.urls.defaults import *
from bookmarks.views import *
import os.path
from django.views.generic.simple import direct_to_template 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

site_media = os.path.join( 
  os.path.dirname(__file__), 'site_media' 
) 

urlpatterns = patterns('',
  # Browsing
  (r'^$', main_page),
  (r'^user/(\w+)/$', user_page),
  # Session management
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', logout_page),
  (r'^register/$', register_page),
  (r'^register/success/$', direct_to_template,
     { 'template': 'registration/register_success.html' }),
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
     { 'document_root': site_media }),
  # Account management
  (r'^save/$', bookmark_save_page),
      
    # Example:
    # (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
