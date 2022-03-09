from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'category')
        prepopulated_fields = {'slug': ('title',)}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)