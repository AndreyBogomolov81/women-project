from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import center

from women.models import Women, Category

menu_0 = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
my_date = datetime.now()

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h4>Анджелина Джоли</h4> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

# cats_db = [
#     {'id': 1, 'name': 'Актрисы'},
#     {'id': 2, 'name': 'Певицы'},
#     {'id': 3, 'name': 'Спортсменки'},
# ]


# Create your views here.
class MyClass:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coord(self):
        return f'x = {self.x}, y = {self.y}'


# def index(request: HttpRequest) -> HttpResponse:
#     # t = render_to_string('women/index.html')
#     # return HttpResponse(t)
#     context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'float': 28.68,
#         'lst': [1, 2, 'abc', True],
#         'set': {1, 2, 3, 4, 5},
#         'dict': {'key1': 'value1', 'key2': 'value2'},
#         'obj': MyClass(10, 20),
#         'my_date': my_date,
#         'value': True
#     }
#     return render(request, 'women/index.html', context=context)

def index(request: HttpRequest) -> HttpResponse:
    posts = Women.published.all()
    context = {
        'title': 'главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
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

    return render(request, 'women/biography.html', context=context)


def about(request):
    context = {'title': 'страница о сайте', 'menu': menu}
    return render(request, 'women/about.html', context=context)


# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Categories</h1><p>Cat id: {cat_id}')


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


# def posts_list(request, year):
#     if year in range(1990, 2024):
#         return HttpResponse(f'posts: {year}')
#     else:
#         raise Http404()

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=data)


def addpage(request):
    return HttpResponse('<h1>Добавление статьи</h1>')


def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def post_archive(request, year, post_id):
    return HttpResponse(f'Year: {year} Post`s id {post_id}')


def post_details(request, year, post_id):
    # url = reverse('cats_id', kwargs={'year': year, 'post_id': post_id})
    url = reverse('cats_id', kwargs={'year': year, 'post_id': post_id})
    print(url)
    return redirect(url)


def categories(request, year, post_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories</h1><p>Year: {year} Post ID: {post_id}')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

    context = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=context)
