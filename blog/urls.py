from django.urls import path
from .views import blog_list_view, create_blog_view

urlpatterns = [
    path('blogs/', blog_list_view, name='blog_list'),
    path('create-blog/', create_blog_view, name='create_blog'),
]
