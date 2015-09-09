from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from ..models import Page


class PageViewTestCase(TestCase):

    def setUp(self):
        self.c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.page = self._create_page()

    def tearDown(self):
        ...    
    
    def test_get_page_view(self):

        c = self.c

        response = c.get('/pages/home')
        
        self.assertEquals(response.status_code,200,'home page')
        
        self.assertTrue(isinstance(response.context['page'], Page))
        
        self.assertIn(self.page.content, str(response.content))

    def test_get_invalid_page_view(self):

        c = self.c

        response = c.get('/pages/non-existe-page')
        
        self.assertEquals(response.status_code,200,'should not give any error')
        
    def _create_page(self):
        
        page = Page(relative_url='home',content='<p>This is the page content</p>',template='page-default.html')
        page.save();
        return page