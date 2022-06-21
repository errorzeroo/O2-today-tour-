from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from tour import settings


class adddate(models.Model):
    during = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        # db_table = 'schedule_app_adddate'


class hotplace(models.Model):
    tour = models.ForeignKey(adddate, on_delete=models.CASCADE)
    days = models.IntegerField()
    tour_place = models.CharField(max_length=100)

    class Meta:
        managed = True
