import pdb

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.base import View
# Create your views here.

from .models import Page

class PageView(View):
    
    def get(self, request, relative_url):

        relative_url = relative_url.split('/')[-1]
        #pdb.set_trace()
        if not Page.objects.filter(relative_url=relative_url).exists():
            return render_to_response('page-does-not-exist.html')

        
        page = Page.objects.get(relative_url=relative_url)
        page.access_count += 1
        page.save()
        
        request_context = RequestContext(request,{'page':page})
        
        return render_to_response(page.template, request_context)