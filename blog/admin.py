from django.contrib import admin
from django.db.models import fields
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'author','published_date')
    list_display_links=('id', 'title')
    search_fields=('title', 'text')
    list_editable=('published_date',)
    list_filter=('create_date', 'published_date')

admin.site.register(Post, PostAdmin)