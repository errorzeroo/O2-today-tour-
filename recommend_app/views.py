from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'recommend_app/recommend_list.html')
