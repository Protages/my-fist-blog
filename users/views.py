from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeDoneView as BasePasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from .forms import UserCreationForm, UserProfileForm
from .models import User


class RegistrationView(View):
    template_name = 'registration/registration.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        form = UserCreationForm(request.POST)
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'registration/profile.html'

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return render(request, self.template_name, {'form': form})
            

class PasswordChangeDoneView(BasePasswordChangeDoneView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(self, request, *args, **kwargs)


class WatchUerProfileView(View):
    template_name = 'registration/show_user_profile.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        context = {
            'user_profile': user,
        }
        return render(request, self.template_name, context)


class AllUsersView(View):
    template_name = 'registration/all_users.html'

    def get(self, request):
        users = User.objects.all().annotate(posts=Count('post')).order_by('-posts')
        context = {
            'users': users
        }
        return render(request, self.template_name, context)