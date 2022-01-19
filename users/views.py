from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeDoneView as BasePasswordChangeDoneView

from .forms import UserCreationForm, UserProfileForm

class Registration(View):
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
        return render(request, self.template_name, {'form': form})


class Profile(View):
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