# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse
from tvtort.models import SeriesCountry, SeriesEpisode
import datetime
from datetime import date

# comment
def archive(request):
    t = loader.get_template("tvtort/base.html")
    return HttpResponse(t)

def base(request):
    endDate = date.today()
    startDate = endDate - datetime.timedelta(days=5)

    last_episodes = SeriesEpisode.objects.filter(addDate__range=[startDate, endDate])
    alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
                "Х", "Ц", "Ч", "Ш", "Щ", "Э", "Ю", "Я"]
    alphabet.sort()

    t = loader.get_template("tvtort/base_content.html")
    html = t.render(Context({"last_episodes": last_episodes, "alphabet": alphabet}))
    return HttpResponse(html)


def index(request):
    latest_countries = SeriesCountry.objects.order_by()
    template = loader.get_template("index.html")
    context = Context({"latest_countries": latest_countries})
    return HttpResponse(template._render(context))


def detail(request, num):
    country = get_object_or_404(SeriesCountry, pk=num)
    return render(request, 'tvtort/detail.html', {"country": country})


def results(request, num):
    return HttpResponse("You're looking at the results of tvtort %s." % num)


def vote(request, num):
    return HttpResponse("You're voting on tvtort %s." % num)


