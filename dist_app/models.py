from django.db import models

# Create your models here.

class Wifi(models.Model):
    place = models.CharField(max_length=200)         # 설치장소명
    latitude = models.CharField(max_length=20)         # 위도
    longitude = models.CharField(max_length=20)        # 경도
    address = models.CharField(max_length=200)     # 설치장소상세