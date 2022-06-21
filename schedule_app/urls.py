from django.urls import path
from . import views

app_name = 'schedule_app'

urlpatterns = [
    path("index/", views.index, name='index'),
    path("list/", views.schedulelist, name='list'),
    path("create/", views.create, name='create'),
    path("day/", views.day),
    path("finallist/", views.finallist)
]