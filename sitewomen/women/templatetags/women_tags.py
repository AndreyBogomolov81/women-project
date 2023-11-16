from django import template

import women.views as views

register = template.Library()  # для последующей регистрации тегов


# функция, которая будет представлять наш новый тег
@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db  # возвращает список категорий, прописанных в модуле women.views


@register.simple_tag()
def get_default_title(title='Заголовок по умолчанию'):
    return title


@register.inclusion_tag('women/list-categories.html')
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selected': cat_selected}


