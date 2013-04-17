from django.template import loader
from django.http import HttpResponse

def archive(request):
    t = loader.get_template("base.html")
    return HttpResponse(t)

def index(request):
    return HttpResponse("HelloWorld!")

def detail(request, num):
    return HttpResponse("You're looking at tvtort %s." % num)

def results(request, num):
    return HttpResponse("You're looking at the results of tvtort %s." % num)

def vote(request, num):
    return HttpResponse("You're voting on tvtort %s." % num)
