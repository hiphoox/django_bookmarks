# Create your views here.
from django.http import HttpResponse 
from django.template import Context 
from django.template.loader import get_template 
from django.http import HttpResponse, Http404 
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def main_page(request): 
  return render_to_response( 
    'main_page.html', 
    { 'user': request.user } 
  ) 
  
def user_page(request, username): 
    try: 
      user = User.objects.get(username=username) 
    except: 
      raise Http404('Requested user not found.') 
    bookmarks = user.bookmark_set.all() 
    template = get_template('user_page.html') 
    variables = Context({ 
      'username': username, 
      'bookmarks': bookmarks 
    }) 
    output = template.render(variables) 
    return HttpResponse(output)
    
def logout_page(request): 
  logout(request) 
  return HttpResponseRedirect('/') 
    