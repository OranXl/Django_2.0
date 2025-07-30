from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForms, LoginForm, RegistrationFomr
from django.contrib.auth import login, logout


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
    ext_post = Post.objects.all().order_by('-wathed')[:4]
    context ={
        'title': article.title,
        'post': article,
        'ext_post': ext_post
    }
    return render(request, template_name='cooking/article_detail.html', context=context)


def add_post(request):
    """Добавление статьи пользоваелем"""
    if request.method == 'POST':
        form = PostAddForms(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)

    else:
        form = PostAddForms()

    context = {'form': form,
               'title': 'Добавить статью'
    }
    return render(request, template_name='cooking/article_add_form.html', context=context)
     


def user_login(request):
    """Аунтефикация пользователя"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': "Авторизация пользователя",
        'form': form
    }
    return render(request, template_name='cooking/login_form.html', context=context)

def user_logout(request):
    """Выход пользователя"""
    logout(request)
    return redirect('index')

def register(request):
    """Регистрация"""
    if request.method == 'POST':
        form = RegistrationFomr(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationFomr()

    context = {
        'title': 'Регистрация пользователя',
        'form': form
    }
    return render(request, template_name='cooking/register.html', context=context)