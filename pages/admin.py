from django.contrib import admin

from .models import Page, MetaTag

class PageAdmin(admin.ModelAdmin):
    list_filter = ('title','relative_url','template','access_count')
    list_display = ('title','relative_url','template','access_count')
    search_fields = ['title','relative_url','template','access_count']

admin.site.register(Page, PageAdmin)

class MetaTagAdmin(admin.ModelAdmin):
    list_filter = ('page','name','property','content')
    list_display = ('page','name','property','content')
    search_fields = ['name','property','content']
    
admin.site.register(MetaTag, MetaTagAdmin)