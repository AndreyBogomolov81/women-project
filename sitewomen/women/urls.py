from django.urls import path, re_path, register_converter

from women import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    path('cats/posts/<int:cat_id>/<slug:cat_slug>/', views.categories_by_double, name='posts'),
    path('archive/<year4:year>/', views.categories_by_re, name='archive'),
    path('detail/', views.post_detail, name='details'),
    path('posts/<int:year>', views.posts_list, name='posts'),
    path('about/', views.about, name='about'),
    path('biography/', views.biography, name='bio'),
]