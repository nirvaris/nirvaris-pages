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
        context_variables = {
            'page': page,
            'title': page.title,
        }
        meta_data_locals = [
            {
                'name':'keywords',
                'content':'some key words from view'
            },
        ]

        for meta_tag in page.meta_tags.all():
            if meta_tag.property:
                meta_data_locals.append({
                    'property': meta_tag.property,
                    'content': meta_tag.content,
                })

            if meta_tag.name:
                meta_data_locals.append({
                    'name': meta_tag.name,
                    'content': meta_tag.content,
                })

        context_variables['meta_data_locals'] = meta_data_locals

        request_context = RequestContext(request, context_variables)

        return render_to_response(page.template, request_context)
