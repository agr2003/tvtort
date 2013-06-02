# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tvtort import views
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.base, name='base'),
                       # ex: /polls/5/
                       url(r'^(?P<letter>\w{1})/$', views.seriesByLetter, name='detail'),
                       # include the lookup urls
                       (r'^admin/lookups/$', include(ajax_select_urls)),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )




