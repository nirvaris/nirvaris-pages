from django.db import models

# Create your models here.

class Page(models.Model):
    relative_url = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=70, null=False)
    template = models.CharField(max_length=50, null=False, default='page-default.html')
    content = models.TextField(null=False)
    access_count = models.BigIntegerField(default=0,null=False)   
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.relative_url
        
class MetaTag(models.Model):
    name = models.CharField(max_length=70, null=True)
    property = models.CharField(max_length=70, null=True)
    content  = models.CharField(max_length=155, null=False)
    page = models.ForeignKey('Page', related_name='meta_tags', null=False)