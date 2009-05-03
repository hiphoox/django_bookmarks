import os
import sys

#You need to set the path up before importing the WSGIHandler module
sys.path = ['/home/experior/webapps/django_trunk', '/home/experior/webapps/django_trunk/lib/python2.5'] + sys.path
sys.path.append('/home/experior/webapps/django_trunk/django_bookmarks/')

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_bookmarks.settings'
application = WSGIHandler()
