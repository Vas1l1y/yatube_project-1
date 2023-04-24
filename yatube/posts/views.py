from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница с постами отфильтрована по группам
def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')
