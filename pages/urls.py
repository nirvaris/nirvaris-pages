from django.conf.urls import url

from .views import PageView

urlpatterns = [
    url(r'^(?P<relative_url>.*)$', PageView.as_view(), name='page'),

]