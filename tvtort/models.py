from django.db import models
from django.db.models import permalink

from tvtort.fields import ThumbnailImageField

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})

        #
class SeriesGenre(models.Model):
    title = models.CharField(max_length=200)
    titleRu = models.CharField(max_length=200)

class SeriesCountry(models.Model):
    title = models.CharField(max_length=200)
    titleRus = models.CharField(max_length=200)
    a2 = models.CharField(max_length=2)
    a3 = models.CharField(max_length=3)
    numberCode = models.IntegerField()

    # .
class SeriesPersonRole(models.Model):
    title = models.CharField(max_length=200)


class IMDB(models.Model):
    url = models.CharField(max_length=500)
    score = models.IntegerField()

# .
class SeriesPerson(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    roles = models.ManyToManyField(SeriesPersonRole)
    portfolioURL = models.CharField(max_length=500)

#
class SeriesDescription(models.Model):
    title = models.CharField(max_length=350)
    originalTitle = models.CharField(max_length=350)
    titleRU = models.CharField(max_length=350)
    originalTitleRU = models.CharField(max_length=350)
    coverPath = models.CharField(max_length=300)
    genres = models.ManyToManyField(SeriesGenre)
    countries = models.ManyToManyField(SeriesCountry)
    releaseDate = models.DateField()
    director = models.ManyToManyField(SeriesPerson, related_name='seriesdescription_director')
    cast = models.ManyToManyField(SeriesPerson, related_name='seriesdescription_actor')
    imdb = models.ForeignKey(IMDB)










