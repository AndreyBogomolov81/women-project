from django import template

import women.views as views
from women.models import Category, TagPost

register = template.Library()  # для последующей регистрации тегов


# функция, которая будет представлять наш новый тег
# @register.simple_tag(name='getcats')
# def get_categories():
#     return views.cats_db  # возвращает список категорий, прописанных в модуле women.views


# @register.simple_tag()
# def get_default_title(title='Заголовок по умолчанию'):
#     return title


@register.inclusion_tag('women/list-categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list-tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}
