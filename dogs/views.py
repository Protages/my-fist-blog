from django.shortcuts import render, get_object_or_404
from .models import Dog

# Create your views here.
def dogs_list(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/dogs_list.html', {'dogs': dogs})

def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogs/dog_detail.html', {'dog': dog})