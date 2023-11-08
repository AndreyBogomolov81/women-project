from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Main page</h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>Cat id: {cat_id}')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Categories</h1><p>Cat slug: {cat_slug}')


def categories_by_re(request, year):
    return HttpResponse(f'<h1>Categories</h1><p>Year: {year}')

def categories_by_double(requests, cat_id, cat_slug):
    return HttpResponse(f'<h1>Categories by double</h1><p>Cat_id: {cat_id} Cat_slug: {cat_slug}')