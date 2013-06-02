# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse
from tvtort.models import SeriesCountry, SeriesEpisode, SeriesDescription, SeriesName
import datetime
from datetime import date

alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
            "Х", "Ц", "Ч", "Ш", "Щ", "Э", "Ю", "Я"]

# comment
def archive(request):
    t = loader.get_template("tvtort/base.html")
    return HttpResponse(t)


def base(request):
    # загружаем серии добавленные за последние пять дней
    endDate = date.today()
    startDate = endDate - datetime.timedelta(days=5)
    # сортируем в реверсивном порядке, последние наверх
    last_episodes = SeriesEpisode.objects.filter(addDate__range=[startDate, endDate]).order_by("-addDate")

    alphabet.sort()

    t = loader.get_template("tvtort/base_content.html")
    html = t.render(Context({"last_episodes": last_episodes, "alphabet": alphabet}))
    return HttpResponse(html)


def index(request):
    latest_countries = SeriesCountry.objects.order_by()
    template = loader.get_template("index.html")
    context = Context({"latest_countries": latest_countries})
    return HttpResponse(template._render(context))


def seriesByLetter(request, letter):
    # загружаем название сериала по первой букве
    seriesNames = SeriesName.objects.filter(titleRU__regex=r"^[%s]+" % letter)
    seriesDescriptionResult = []
    # получаем сериал по имени
    # todo разобраться в возможности добавления сразу списка
    for seriesName in seriesNames:
        for seriesDescription in seriesName.seriesdescription_set.all():
            seriesDescriptionResult.append(seriesDescription)

    t = loader.get_template("tvtort/base_series_by_name.html")
    html = t.render(Context({"series_descriptions": seriesDescriptionResult, "alphabet": alphabet}))
    return HttpResponse(html)

def searchByName(request, searchString):
    seriesNames = SeriesName.objects.filter(titleRU__regex=r"^+[%s]+" % searchString)


def results(request, num):
    return HttpResponse("You're looking at the results of tvtort %s." % num)


def vote(request, num):
    return HttpResponse("You're voting on tvtort %s." % num)


