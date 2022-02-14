from django.contrib import admin
from django.db.models import fields

from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'author','category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('category',)
    list_filter = ('create_date', 'published_date')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'create_date', 'edit_date')
    search_fields = ('author', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}