from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Поля которые будут отображаться в API"""

    class Meta:
        model=Post
        fields = ('title', 'category', 'craete_at', 'content', 'author')
