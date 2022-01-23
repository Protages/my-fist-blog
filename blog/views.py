from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.filter(comment=None)
    if request.method == 'POST':
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.create_date = datetime.now()
            comment.save()
    form_comment = CommentForm()  
    return render(request, 'blog/post_detail.html', {
        'post': post, 
        'comments': comments, 
        'form_comment': form_comment
        })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form})


def comment_edit(request, pk, post_pk=1):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.edit_date = datetime.now()
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'blog/comment_edit.html', {'form': form})


class SearchView(View):
    template_name = 'blog/search.html'

    def get(self, request):
        query = request.GET['q']
        if not(query.isspace() or query == ''):
            posts = Post.objects.filter(title__icontains=query)
        else:
            posts = None
        context = {
            'posts': posts,
            'query': query
        }
        return render(request, self.template_name, context)


class AnswerForCommentView(View):
    template_name = 'blog/comment_answer.html'

    def get(self, request, post_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        form = CommentForm()
        context = {
            'comment': comment,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, post_pk, comment_pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=post_pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.comment = Comment.objects.get(pk=comment_pk)
            comment.create_date = datetime.now()
            comment.save()
            return redirect('post_detail', pk=post_pk)
        return render(request, self.template_name, {'form': form})