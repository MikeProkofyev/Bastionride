# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('mainapp.views',
    url(r'^$', 'index', name='index'),
)
