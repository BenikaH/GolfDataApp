from django.conf import urls
from django.urls import path
from Home import views


urlpatterns = [
    path('homepage.html', views.home_page)
]
