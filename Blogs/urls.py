from django.conf.urls import url
from django.urls import path
from Blogs import views


urlpatterns = [
    path('blog_posts.html', views.blog_posts, name='blog_posts'),
    path('blog_form.html', views.blog_post_form, name='blog_post_form'),
]