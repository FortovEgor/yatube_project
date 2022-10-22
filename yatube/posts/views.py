from django.shortcuts import render

# Create your views here.


# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'переданный параметр: {slug}')