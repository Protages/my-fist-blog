from django.urls import path, include

from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
    path('search/', SearchView.as_view(), name='search'),
    path('post_new/', EditCreatePostView.as_view(), name='post_new'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:post_slug>/edit/', EditCreatePostView.as_view(), name='post_edit'),
    path('post/<slug:post_slug>/comment_add/', AddCommentView.as_view(), name='comment_add'),
    path('post/<slug:post_slug>/comment_edit/<int:pk>/', comment_edit, name='comment_edit'),
    path('post/<slug:post_slug>/comment/<int:comment_pk>/answer/',
        AnswerForCommentView.as_view(),
        name='comment_answer'
    ),
]