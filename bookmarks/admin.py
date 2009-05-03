from bookmarks.models import Link, Bookmark, Tag
from django.contrib import admin

class BookmarkAdmin(admin.options.ModelAdmin):
  list_display = ('title', 'link','user') 
  list_filter = ('user', ) 
  ordering = ('title', ) 
  search_fields = ('title', )
   
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(Bookmark, BookmarkAdmin)
