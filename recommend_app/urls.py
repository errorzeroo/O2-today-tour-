from django.urls import path
from . import views

app_name = 'recommend_app'

urlpatterns = [
    path("index/",views.index, name='index')
]