from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("Welcome to the course!")


def say_bye(request):
    context = {'name': 'Mohamamd'}
    return render(request, 'bye.html', context=context)