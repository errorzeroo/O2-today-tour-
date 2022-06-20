from django.shortcuts import render
from django.http import HttpResponse
from .models import Wifi
import csv


def index(request):
    wifiList = Wifi.objects.all()
    context = {"wifiList" : wifiList}
    return render(request, 'dist_app/dist_app.html', context)

def detail(request, category):
    wifiList = Wifi.objects.filter(svcProvdNm=category)
    context = {'centerLat': wifiList.latitude, 'centerLon': wifiList.longitude, 'wifiList': wifiList}
    return render(request, "dist_app/dist_app.html", context)



def marker(request):
    return render(request, 'dist_app/dist_app_marker.html')

def bulk_import(request):
    CSV_PATH = 'static/jeju_copy.csv'

    with open(CSV_PATH, newline='', encoding='cp-949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Wifi.objects.create(

                place = row['place'],
                latitude = row["lat"],
                longitude = row["lon"],
                address = row["address"]
            )
    return