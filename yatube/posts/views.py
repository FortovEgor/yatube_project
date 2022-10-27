# from re import template
from django.shortcuts import render

# Create your views here.


# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    # return HttpResponse('Ты <i>не можешь</i> получить правильные '
    #                     '<b>ответы</b>,<br> если у тебя нет правильных '
    #                     '<s>вопросов</s> запросов.')
    template = 'posts/index.html'
    context = {
        'title': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


# Страница group_list
def group_list(request):
    # return HttpResponse('Ты <i>не можешь</i> получить правильные '
    #                     '<b>ответы</b>,<br> если у тебя нет правильных '
    #                     '<s>вопросов</s> запросов.')
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)


# Страница со списком мороженого
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    # return HttpResponse(f'переданный параметр: {slug}')
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)