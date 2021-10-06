from django.shortcuts import render, get_object_or_404
from .models import Cat

# Create your views here.
def cats_list(request):
    cats = Cat.objects.all()
    return render(request, 'cats/cats_list.html', {'cats': cats})

def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cats/cat_detail.html', {'cat': cat})