from django.shortcuts import render
from .models import Category, Post
from django.db.models import F




def index(request):
    '''Для главной страницы'''
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts,
        'categories': categories
    }
    return render(request, template_name='cooking/index.html', context=context)


def category_list(request, pk):
    """Реакция на нажатие кнопки каегории"""
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories
    }
    return render(request, template_name='cooking/index.html', context=context)




def post_detail(request, pk):
    """Страница статьи"""
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(wathed=F('wathed') + 1)
    context ={
        'title': article.title,
        'post': article
    }
    return render(request, template_name='cooking/article_detail.html', context=context)