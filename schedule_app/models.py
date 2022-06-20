from django.db import models


# Create your models here.

class adddate(models.Model):
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'schedule_app_adddate'
