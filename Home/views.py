from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404


def home_page(request):
    return render(request, 'Home/homepage.html', context=None)
