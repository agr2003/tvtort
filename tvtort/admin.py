__author__ = 'agr'

from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from tvtort.models import SeriesDescription, SeriesPerson, IMDB, SeriesCountry, SeriesGenre, SeriesName, SeriesRating, SeriesSeasonRating, SeriesEpisode, SeriesSeason



admin.site.register(SeriesPerson)
admin.site.register(IMDB)
admin.site.register(SeriesCountry)
admin.site.register(SeriesGenre)
class SeriesNameAdmin(admin.ModelAdmin):
    pass
admin.site.register(SeriesName, SeriesNameAdmin)
admin.site.register(SeriesRating)
admin.site.register(SeriesSeasonRating)
admin.site.register(SeriesEpisode)
admin.site.register(SeriesSeason)
class SeriesDescriptionAdmin(AjaxSelectAdmin):
    form = make_ajax_form(SeriesName,{'titleRU':'seriesName'})
admin.site.register(SeriesDescription)

# # subclass AjaxSelectAdmin
# class SeriesNameAdmin(AjaxSelectAdmin):
#     # create an ajax form class using the factory function
#     #                     model,fieldlist,   [form superclass]
#     form = make_ajax_form(SeriesName, {'titleRU': 'seriesName'})
# admin.site.register(SeriesName, SeriesNameAdmin)





