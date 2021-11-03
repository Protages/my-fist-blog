from django.contrib import admin
from django.db.models import fields
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'author','published_date')
    list_display_links=('id', 'title')
    search_fields=('title', 'text')
    list_editable=('published_date',)
    list_filter=('create_date', 'published_date')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'create_date', 'edit_date')
    search_fields = ('author', 'text')

admin.site.register(Comment, CommentAdmin)