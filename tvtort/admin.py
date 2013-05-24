__author__ = 'agr'

from django.contrib import admin
from tvtort.models import Item, Photo, SeriesDescription, SeriesPerson, IMDB, SeriesPersonRole, SeriesCountry, SeriesGenre


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    fields = ['description', 'name']

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
admin.site.register(SeriesDescription)
admin.site.register(SeriesPerson)
admin.site.register(IMDB)
admin.site.register(SeriesPersonRole)
admin.site.register(SeriesCountry)
admin.site.register(SeriesGenre)






