from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse
from tvtort.models import SeriesCountry


def archive(request):
    t = loader.get_template("base.html")
    return HttpResponse(t)

def base(request):
    t = loader.get_template("base.html")
    return HttpResponse(t)


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


