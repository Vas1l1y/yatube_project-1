from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('pub_date')[:10]
    context = {
        'posts': posts,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
