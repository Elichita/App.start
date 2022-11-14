from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 5 * 5
    return render(request, 'about.html', {'hello': a})


def home(request):
    return HttpResponse('NO')