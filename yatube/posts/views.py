# from re import template
from django.shortcuts import render

# Create your views here.


# posts/views.py
from django.http import HttpResponse
from .models import Post


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений
    # к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


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