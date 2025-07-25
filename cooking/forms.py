from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class PostAddForms(forms.ModelForm):
    """Форма для добавления новой статьи для пользователя"""
    class Meta:
        """Мета класс, указывающий поведенческий характер, чертёж для класса"""
        model = Post
        fields = ('title', 'content', 'photo', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

class LoginForm(AuthenticationForm):
    """Форма для аунтефикации пользователя"""
    username = forms.CharField(label='Имя пользователя',
                               max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               max_length=150,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))