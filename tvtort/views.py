from django.template import loader, Context
from django.http import HttpResponse

def archive(request):
    t = loader.get_template("base.html")
    return HttpResponse(t)
