from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Main page</h1>')


def categories(request, cat_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories</h1><p>Cat id: {cat_id}')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Categories</h1><p>Cat slug: {cat_slug}')


def categories_by_re(request, year):
    if year > 2023:
        # return redirect('/detail/', permanent=True) # use URL address
        # return redirect(index) # use view function
        # return redirect('home')  # use the route name, recommended
        # url = reverse('/') +
        # return redirect(reverse('home')) +
        # return redirect(reverse(categories, args=(1,))) +
        return redirect(reverse('cats_id', args=[1]))

    return HttpResponse(f'<h1>Archive: </h1><p>Year: {year}')


def categories_by_double(requests, cat_id, cat_slug):
    return HttpResponse(f'<h1>Categories by double</h1><p>Cat_id: {cat_id} Cat_slug: {cat_slug}')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def post_detail(request):
    if request.GET:
        temp = [f'{k}={v}' for k, v in request.GET.items()]
        response = '|'.join(temp)
    else:
        response = 'GET is empty'

    return HttpResponse(response)


def posts_list(request, year):
    if year in range(1990, 2024):
        return HttpResponse(f'posts: {year}')
    else:
        raise Http404()


def about_view(request):
    return HttpResponse('<h1>Hello from about</h1>')
