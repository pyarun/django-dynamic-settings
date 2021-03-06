# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from dynamicsettings import views

urlpatterns = patterns('',
    url(r'^$', views.dynamicsettings_index, name='dynamicsettings_index'),
    url(r'^set/$', views.dynamicsettings_set, name='dynamicsettings_set'),
    url(r'^reset/$', views.dynamicsettings_reset, name='dynamicsettings_reset'),   
)