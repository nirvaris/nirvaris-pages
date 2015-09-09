from django.conf.urls import url

from django.conf.urls import include, url
from django.contrib import admin

from .views import PageView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<relative_url>.*)$', PageView.as_view(), name='page'),

]