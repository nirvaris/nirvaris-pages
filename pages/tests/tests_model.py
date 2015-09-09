from django.test import TestCase

from ..models import Page, MetaTag

class PageModelTestCase(TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...
        
    def test_create_page(self):
        
        page = Page(relative_url='home',content='<p>This is the page content</p>',template='page-default.html')
        page.save();
        return page
    
    def test_create_meta_tag_key(self):
        
        page = self.test_create_page()
        meta_tag = MetaTag(page=page, name='keywords',content='some key words')
        meta_tag.save()
        
        return meta_tag
        