from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, '404.html', {'ex': exception} , status=404)


def page_500(request):
    return render(request, '500.html', status=500)