from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import center

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
my_date = datetime.now()

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Бтография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


# Create your views here.
class MyClass:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coord(self):
        return f'x = {self.x}, y = {self.y}'


def index(request: HttpRequest) -> HttpResponse:
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.68,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 4, 5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': MyClass(10, 20),
        'my_date': my_date,
        'value': True
    }
    return render(request, 'women/index.html', context=context)


def biography(request):
    context = {
        'title': 'биография',
        'menu': menu,
        'posts': data_db,
        'show_menu': True
    }

    data1 = {
        'form_data': {'is_data': True, 'username': 'root', 'password': '1234'},
    }

    data = {
        'is_draft': False,
        'content': "super content",
        'title': "super post",
    }

    return render(request, 'women/biography.html', context=data)


def about(request):
    context = {'title': 'Страница о сайте'}
    return render(request, 'women/about.html', context=context)


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
