# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tvtort import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.base, name='base'),
                       # ex: /polls/5/
                       url(r'^(?P<letter>\w{1})/$', views.detail, name='detail'),
                       # ex: /polls/5/results/
                       url(r'^(?P<num>\d+)/results/$', views.results, name='results'),
                       # ex: /polls/5/vote/
                       url(r'^(?P<num>\d+)/vote/$', views.vote, name='vote'),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )




