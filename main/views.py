from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest

def index(request):
    return render(request, "main/index.html")

def products(request):
    return render(request, "main/products.html")