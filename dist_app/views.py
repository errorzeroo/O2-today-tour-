from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'dist_app/dist_app.html')