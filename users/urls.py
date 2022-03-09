from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/<slug:username>/', views.WatchUerProfileView.as_view(), name='show_user_profile'),
    path('all/', views.AllUsersView.as_view(), name='all_users'),
]