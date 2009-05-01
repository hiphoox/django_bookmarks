# Create your views here.
from django.http import HttpResponse 
from django.template import Context 
from django.template.loader import get_template 

def main_page(request): 
  template = get_template('main_page.html') 
  variables = Context({ 
    'head_title': 'Django Bookmarks', 
    'page_title': 'Welcome to Django Bookmarks', 
    'page_body': 'Where you can store and share bookmarks!' 
  }) 
  output = template.render(variables) 
  return HttpResponse(output)