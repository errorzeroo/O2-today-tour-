from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
# from django_filters
from datetime import date, timedelta

from .models import adddate


def index(request):
    return render(request, 'schedule_app/schedule_list.html')


def createdate(request):
    date = adddate(startdate=request.GET.get('startdate'), enddate=request.GET.get('enddate'))
    date.save()

    return redirect('/schedule_app/list')


# class dateList(ListView):
#     model = adddate
#     template_name = 'schedule_app/schedule_list.html'

def schedulelist(request):
    schedule_list = adddate.objects.order_by('startdate')
    return render(request, 'schedule_app/schedule_list.html', {'schedule_list': schedule_list})


def date_minus(request):
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    daterange = adddate.objects.filter(daterange_date__range=[startdate, enddate]) # 날짜 범위 계산하는 식
    return render(request, 'schedule_app/schedule_list.html', {'daterange': daterange})
