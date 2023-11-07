from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Main page</h1>')

def categories(request):
    return HttpResponse('<h1>Categories</h1>')