from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def hello(request):
    hello = "Hello world"
    return HttpResponse(hello)

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def inicio(request):
    inicio = "Esto es el inicio"
    return HttpResponse(inicio)
