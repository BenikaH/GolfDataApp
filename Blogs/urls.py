from django.conf import urls
from django.urls import path
from . import views


urlpatterns = [
    path('blogs.html', views.blog_posts),
]