from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
from django.db import models 
class Link(models.Model): 
  url = models.URLField(unique=True) 

  def __str__(self): 
     return self.url
     
class Bookmark(models.Model): 
  title = models.CharField(max_length=200) 
  user = models.ForeignKey(User) 
  link = models.ForeignKey(Link)
    
  def __str__(self): 
     return '%s, %s' % (self.user.username, self.link.url) 
    
class Tag(models.Model): 
  name = models.CharField(max_length=64, unique=True) 
  bookmarks = models.ManyToManyField(Bookmark)
  
  def __str__(self): 
     return self.name
