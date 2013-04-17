__author__ = 'agr'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^tvtort/', include('tvtort.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
