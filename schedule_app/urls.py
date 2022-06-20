from django.urls import path
from . import views

app_name = 'schedule_app'

urlpatterns = [
    path("index/", views.index, name='index'),
    path("createdate/", views.createdate, name='createdate'),
    path("list/",views.schedulelist, name='list')
]