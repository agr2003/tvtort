__author__ = 'agr'

from django.contrib import admin
from tvtort.models import Item, ItemAdmin, Photo

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)




