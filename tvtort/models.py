# -*- coding: utf-8 -*-
from django.db import models
import datetime

class SeriesGenre(models.Model):
    title = models.CharField(max_length=200)
    titleRu = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titleRu

class SeriesCountry(models.Model):
    title = models.CharField(max_length=200)
    titleRus = models.CharField(max_length=200)
    a2 = models.CharField(max_length=2)
    a3 = models.CharField(max_length=3)
    numberCode = models.IntegerField()

    def __unicode__(self):
        return self.titleRus


class IMDB(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return self.url

# .
class SeriesPerson(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, default=None)
    portfolioURL = models.URLField()

    def __unicode__(self):
        return u"{0} {1}".format(self.firstname, self.lastname)

#

class SeriesName(models.Model):
    title = models.CharField(max_length=350)
    titleRU = models.CharField(max_length=350)

    def __unicode__(self):
        return u"{0} / {1}".format(self.titleRU, self.title)


class SeriesDescription(models.Model):
    name = models.ForeignKey(SeriesName)
    coverPath = models.FileField(upload_to="photos")
    genres = models.ManyToManyField(SeriesGenre)
    countries = models.ManyToManyField(SeriesCountry)
    releaseDate = models.DateField()
    director = models.ManyToManyField(SeriesPerson, related_name='seriesdescription_director')
    cast = models.ManyToManyField(SeriesPerson, related_name='seriesdescription_actor')
    imdb = models.ForeignKey(IMDB, default=None)
    description = models.CharField(max_length=2000)

    def __unicode__(self):
        return u"{0} / {1}".format(self.name.titleRU, self.name.title)


class SeriesRating(models.Model):
    series = models.ForeignKey(SeriesDescription)
    rating = models.IntegerField()

    def __unicode__(self):
        return u"{0} - {1}".format(self.series.titleRU, self.rating)


class SeriesSeasonRating(models.Model):
    seriesSeason = models.ForeignKey(SeriesDescription)
    rating = models.IntegerField()

    def __unicode__(self):
        return u"{0} - {1}".format(self.seriesSeason.titleRU, self.rating)


class SeriesSeason(models.Model):
    parent = models.ForeignKey(SeriesDescription)
    serialNumber = models.IntegerField()
    description = models.CharField(max_length=2000, default=None)

    def __unicode__(self):
        return u"{0} - {1}".format(self.parent.name.titleRU, self.serialNumber)


class SeriesEpisode(models.Model):
    parent = models.ForeignKey(SeriesSeason)
    title = models.CharField(max_length=350, default=None)
    titleRU = models.CharField(max_length=350, default=None)
    serialNumber = models.IntegerField()
    description = models.CharField(max_length=1200, default=None)
    addDate = models.DateField()
    path = models.FileField(upload_to="video")

    def __unicode__(self):
        return u"{0} - {1} сезон ({2} серия)".format(self.parent.parent, self.parent.serialNumber, self.serialNumber)









