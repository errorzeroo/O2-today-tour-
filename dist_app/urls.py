from django.urls import path
from . import views

app_name = 'dist_app'

urlpatterns = [
    path("index/",views.index, name = "index"),
    path("marker/",views.marker, name = "marker")

]