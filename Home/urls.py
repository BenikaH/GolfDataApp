from django.conf.urls import url
from django.urls import path
from Home import views


urlpatterns = [
    path('homepage.html', views.home_page, name='home_page')
]
