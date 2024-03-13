from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("main/", views.main_view, name="main_view"),
    path("center/",views.center_view,name="center_view"),
    path("south/",views.south_view,name="south_view"),
    path("east/",views.east_view,name="east_view"),
    path("west/",views.west_view,name="west_view"),
    path("north/",views.north_view,name="north_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),  
]