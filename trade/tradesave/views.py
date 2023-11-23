from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.response import TemplateResponse

from .models import *

# Create your views here.

#def index (request):
#    return HttpResponse("<h1>Аукціон index</h1>")

#def user (request):
#    return HttpResponse("<h1>Аукціон user</h1>")

def trade (request):
    return TemplateResponse(request,  "trade.html")

def index (request):
    return TemplateResponse(request,  "index.html")

def user (request):
    return TemplateResponse(request, "user.html")

def contact (request):
    return TemplateResponse(request, "contact.html")

def about (request):
    return TemplateResponse(request, "about.html")


##############################################################
def indexbase(request):
    lots = Lot.objects.all()
    return render(request, 'indexbase.html', {'lots': lots})
    ###return render(request, "indexbase.html")
 
def contactbase(request):
    return render(request, "contactbase.html")

def aboutbase(request):
    return render(request, "aboutbase.html")
 
def tradebase(request):
    return render(request, "tradebase.html")

def userbase(request):
    return render(request, "userbase.html")