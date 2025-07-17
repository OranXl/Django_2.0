from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'wathed', 'is_publeshed', 'category', 'craete_at', 'update_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_publeshed',)
    readonly_fields = ('wathed',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)