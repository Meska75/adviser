from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'blog'),
    path('<str:pid>', blogsingle_view,name='blogsingle'),
    path('category/<str:cat_name>', simple_blog_view,name='category'),
    path('tag/<str:tag_name>', simple_blog_view,name='tag'),
    path('date/<str:date>', simple_blog_view,name='date'),
    path('author/<str:author_username>', simple_blog_view,name='author'),
    path('search/', blog_search,name='search'),
]