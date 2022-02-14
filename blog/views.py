from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView
from django.utils import timezone

from .models import Post, Comment, Category
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context


class CategoryListView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = self.cat.pk
        return context

    def get(self, request, *args, **kwargs):
        self.cat_slug = kwargs['cat_slug']
        self.cat = Category.objects.get(slug=kwargs['cat_slug'])
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(category_id=self.cat.pk)
    

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
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


class EditCreatePostView(LoginRequiredMixin, View):
    template_name_edit = 'blog/post_edit.html'
    template_name_create = 'blog/post_new.html'

    def get(self, request, post_slug=None):
        if post_slug:
            post = get_object_or_404(Post, slug=post_slug)
            form = PostForm(instance=post)
            return render(request, self.template_name_edit, {'form': form})
        else:
            form = PostForm()
            return render(request, self.template_name_create, {'form': form})

    def post(self, request, post_slug=None):
        if post_slug:
            post = get_object_or_404(Post, slug=post_slug)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect(post.get_absolute_url())
            return render(request, self.template_name_edit, {'form': form})
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect(post.get_absolute_url())

            return render(request, self.template_name_create, {'form': form})
        

@login_required
def comment_edit(request, pk, post_slug=None):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.edit_date = datetime.now()
            comment.save()
            return redirect('post_detail', post_slug=post_slug)
    return render(request, 'blog/comment_edit.html', {'form': form})


class SearchView(View):
    template_name = 'blog/search.html'

    def get(self, request):
        query = request.GET['q']
        categories = request.GET.getlist('category')
        if not(query.isspace() or query == ''):
            if categories:
                posts = Post.objects.filter(
                    title__icontains=query, 
                    category__name__in=categories
                )
            else:
                posts = Post.objects.filter(title__icontains=query)
        else:
            posts = None
        context = {
            'posts': posts,
            'query': query,
            'categories': categories
        }
        return render(request, self.template_name, context)


class AnswerForCommentView(View):
    template_name = 'blog/comment_answer.html'

    def get(self, request, post_slug, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        form = CommentForm()
        context = {
            'comment': comment,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, post_slug, comment_pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=post_slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.comment = Comment.objects.get(pk=comment_pk)
            comment.create_date = datetime.now()
            comment.save()
            return redirect(post.get_absolute_url())
        return render(request, self.template_name, {'form': form})


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})


# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_new.html', {'form': form})


# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(instance=post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     return render(request, 'blog/post_edit.html', {'form': form})