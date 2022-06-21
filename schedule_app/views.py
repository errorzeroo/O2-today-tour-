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
    place_list = hotplace.objects.get('tour_place')
    return render(request, 'schedule_app/schedule_list.html',{'place_list': place_list})


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
    # ad = adddate.objects.get(request.POST.get(''))   # adddate id에 해당하는 애를 가져오기
    place = hotplace(tour_place=request.GET.get('place'), days=request.GET.get('num'))
    place.save()

    return redirect('/schedule_app/finallist')
    # return render(request, 'schedule_app/schedule_list.html', {'day': days1})


# def create_hotplace(request):
#     place = hotplace(tour_place=request.GET.get('place'), days=request.GET.get('num'))
#     place.save()
#
#     return redirect('/schedule_app/list')






