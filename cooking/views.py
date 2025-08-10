from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForms, LoginForm, RegistrationFomr
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# def index(request):
#     '''Для главной страницы'''
#     posts = Post.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'title': 'Главная страница',
#         'posts': posts,
#         'categories': categories
#     }
#     return render(request, template_name='cooking/index.html', context=context)

class Index(ListView):
    '''Для главной страницы'''
    model = Post
    context_object_name = 'posts'
    template_name = 'cooking/index.html'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['categories'] = Category.objects.all()
        return context
    



# def category_list(request, pk):
#     """Реакция на нажатие кнопки каегории"""
#     posts = Post.objects.filter(category_id=pk)
#     categories = Category.objects.all()
#     context = {
#         'title': posts[0].category,
#         'posts': posts,
#         'categories': categories
#     }
#     return render(request, template_name='cooking/index.html', context=context)

class ArticleByCategory(Index):
    """Реакция на нажатие кнопки категории"""
    
    def get_queryset(self):
        """Здесь можно переделовать фильтры"""
        return Post.objects.filter(category_id=self.kwargs['pk'], is_publeshed=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        """Для динамических данных"""
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context




# def post_detail(request, pk):
#     """Страница статьи"""
#     article = Post.objects.get(pk=pk)
#     Post.objects.filter(pk=pk).update(wathed=F('wathed') + 1)
#     ext_post = Post.objects.all().exclude(pk=pk).order_by('-wathed')[:5]
#     context ={
#         'title': article.title,
#         'post': article,
#         'ext_post': ext_post
#     }
#     return render(request, template_name='cooking/article_detail.html', context=context)

class PostDetail(DeleteView):
    """Страница статьи"""
    model = Post
    template_name = 'cooking/article_detail.html'

    def get_queryset(self):
        """Для доп. фильтрации"""
        return Post.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Для динамических данных"""
        Post.objects.filter(pk=self.kwargs['pk']).update(wathed=F('wathed') + 1)
        context = super().get_context_data()
        post = Post.objects.get(pk=self.kwargs['pk'])
        ext_post = Post.objects.all().exclude(pk=self.kwargs['pk']).order_by('-wathed')[:5]
        context['title'] = post.title
        context['ext_post'] = ext_post
        return context




# def add_post(request):
#     """Добавление статьи пользоваелем"""
#     if request.method == 'POST':
#         form = PostAddForms(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post.objects.create(**form.cleaned_data)
#             post.save()
#             return redirect('post_detail', post.pk)

#     else:
#         form = PostAddForms()

#     context = {'form': form,
#                'title': 'Добавить статью'
#     }
#     return render(request, template_name='cooking/article_add_form.html', context=context)
     

class AddPost(CreateView):
    """Добавление статьи пользоваелем"""
    form_class = PostAddForms
    template_name = 'cooking/article_add_form.html'
    extra_context = {'title': 'Добавить статью'}

class PostUpdate(UpdateView):
    """Изменение статьи"""
    model = Post
    form_class = PostAddForms
    template_name = 'cooking/article_add_form.html'
    extra_context = {'title': 'Изменения статьи'}



class Postdelet(DeleteView):
    """Удаление статьи"""
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'
    extra_context = {'title': 'Удаление статьи'}






def user_login(request):
    """Аунтефикация пользователя"""
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, message='Вы успешно вошли в аккаунт')
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