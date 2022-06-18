from django.urls import path
from . import views

app_name = 'recommend_app'

urlpatterns = [
    path("",views.index, name='index'),
    path('ver1/', views.ver1, name='ver1'),
    path('ver2/', views.ver2, name= 'ver2'),
    # path('search/', views.SearchFormView.as_view(), name='search')
]