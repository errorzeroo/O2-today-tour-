from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'home_app/index.html')

# def baseTest(request):
#     return render(request, 'home_app/index.html')