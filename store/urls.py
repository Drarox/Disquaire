from django.conf.urls import url
from . import views
from django.urls import include, path  # For django versions from 2.0 and up

urlpatterns = [
    url(r'^$', views.listing, name="listing"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^search/$', views.search, name="search"),
]