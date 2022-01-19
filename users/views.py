from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from .forms import UserCreationForm

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
            