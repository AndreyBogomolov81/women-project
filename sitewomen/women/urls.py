from django.urls import path, re_path, register_converter

from women import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    # path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<int:year>/<int:post_id>/', views.categories, name='cats_id'),
    # path('cats/<int:year>/<int:post_id>/'),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    # path('cats/posts/<int:cat_id>/<slug:cat_slug>/', views.categories_by_double, name='posts'),
    # path('archive/<year4:year>/', views.categories_by_re, name='archive'),
    path('detail/', views.post_detail, name='details'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('biography/', views.biography, name='bio'),
    # path('post/archive/<int:year>/<int:post_id>', views.post_archive, name='post_archive'),
    path('post/archive/<int:year>/<int:post_id>/', views.post_details, name='post_archive'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]