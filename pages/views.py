import pdb

from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

from .models import Page

class PageView(View):

    def get(self, request, relative_url):

        relative_url = relative_url.split('/')[-1]
        #pdb.set_trace()
        if not Page.objects.filter(relative_url=relative_url).exists():
            return render(request,'page-does-not-exist.html')

        page = Page.objects.get(relative_url=relative_url)
        page.access_count += 1
        page.save()
        data_context = {
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

        data_context['meta_data_locals'] = meta_data_locals

        return render(request,page.template, data_context)
