import pdb
import re

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from ..models import Page, MetaTag


class PageViewTestCase(TestCase):

    def setUp(self):
        self.c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.page = self._create_page()

    def tearDown(self):
        ...

    def test_get_page_view(self):

        c = self.c

        response = c.get('/pages/home')

        self.assertEquals(response.status_code, 200, 'home page')

        self.assertTrue(isinstance(response.context['page'], Page))

        self.assertTrue(any(self.page.template in t.name for t in response.templates))

        content = str(response.content)

        self.assertIn(self.page.content, content)

        self.assertTrue(re.search(re.compile('<title>.*' + self.page.title + '.*</title>'), content),
        'page title does not match')

    def test_get_page_meta_tags(self):

        c = self.c

        response = c.get('/pages/home')

        content = str(response.content)

        self.assertTrue(re.search(re.compile('<meta.+?name="keywords"'), content),
        'Meta tag name not found')

        self.assertTrue(re.search(re.compile('<meta.+?name="description"'), content),
        'Meta tag description not found')

        #pdb.set_trace()
        self.assertTrue(re.search(re.compile('<meta.+?property="twitter:card"'), content),
        'Meta tag twitter:card not found')

    def test_get_invalid_page_view(self):

        c = self.c

        response = c.get('/pages/non-existe-page')

        self.assertEquals(response.status_code,200,'should not give any error')

        self.assertTrue(any('page-does-not-exist.html' in t.name for t in response.templates))

    def _create_page(self):

        page = Page(relative_url='home',title='Home Page',content='<p>This is the page content</p>',template='page-default.html')
        page.save();

        meta_tag = MetaTag(page=page, name='keywords',content='some key words')
        meta_tag.save()

        meta_tag = MetaTag(page=page, name='description',content='some description')
        meta_tag.save()

        meta_tag = MetaTag(page=page, property='twitter:card',content='sumary')
        meta_tag.save()

        return page
