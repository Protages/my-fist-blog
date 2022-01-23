from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_pk>/comment_edit/<int:pk>', views.comment_edit, name='comment_edit'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/answer/',
        views.AnswerForCommentView.as_view(),
        name='comment_answer'
    ),
]