from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from . import models
from .models import adddate, hotplace


def index(request):
    return render(request, 'schedule_app/schedule_list.html')


def schedulelist(request):
    during = adddate.objects.filter(author_id='1')

    return render(request, 'schedule_app/schedule_list.html',{'during': during})


def finallist(request):
    model = hotplace
    template_name = 'schedule_app/schedule_list.html'


def create(request):
    during = adddate(during=request.GET.get('during'), author=request.user)
    during.save()

    during1 = request.GET.get('during')
    days = list(range(int(during1)))
    days1 = []
    for i in days:
        days1.append(i + 1)

    return render(request, 'schedule_app/schedule_list.html', {'day': days1,'tour_id':during.pk})
    # return redirect('/schedule_app/list')


def day(request):
    if request.GET.get('place') != None:
        place = Hotplace(tour_place=request.GET.get('place'), days=request.GET.get('test'), tour_id=request.GET.get('fk'))
        place.save()

        return redirect('/schedule_app/finallist')







