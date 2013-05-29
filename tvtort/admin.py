__author__ = 'agr'

from django.contrib import admin
from tvtort.models import SeriesDescription, SeriesPerson, IMDB, SeriesCountry, SeriesGenre, SeriesName, SeriesRating, SeriesSeasonRating, SeriesEpisode, SeriesSeason


admin.site.register(SeriesDescription)
admin.site.register(SeriesPerson)
admin.site.register(IMDB)
admin.site.register(SeriesCountry)
admin.site.register(SeriesGenre)
admin.site.register(SeriesName)
admin.site.register(SeriesRating)
admin.site.register(SeriesSeasonRating)
admin.site.register(SeriesEpisode)
admin.site.register(SeriesSeason)






