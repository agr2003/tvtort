__author__ = 'agr'

from django.contrib import admin
from tvtort.models import Item, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    fields = ['description', 'name']

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)




