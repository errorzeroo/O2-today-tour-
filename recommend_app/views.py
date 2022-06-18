from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'recommend_app/index.html')

def ver1(request):
    return render(request, 'recommend_app/ver1.html')

def ver2(request):
    return render(request, 'recommend_app/ver2.html')
