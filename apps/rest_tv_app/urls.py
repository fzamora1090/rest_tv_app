from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.create),
    url(r'^creating$', views.creating),
    url(r'^shows/(?P<id>\d+)$', views.showing),

    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<id>\d+)/delete$', views.delete),
    
    url(r'^shows/(?P<id>\d+)/updating$', views.updating),








]
