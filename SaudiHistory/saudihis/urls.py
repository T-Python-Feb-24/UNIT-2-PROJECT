from django.urls import path
from . import views

app_name = 'saudihis'

urlpatterns = [
    path('', views.home, name='main'),
    path("middlestate/", views.middlestate, name="middlestate"),
    path("northstate/", views.northstate, name="northstate"),
    path("eaststate/", views.eaststate, name="eaststate"),
    path("westestate/", views.westestate, name="westestate"),
    path("southstate/", views.southstate, name="southstate"),

]
