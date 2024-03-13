from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path("",views.home,name="home_page"),
    path("about/" , views.about_us, name="about_page"),
    path("gallery/" , views.gallery , name="gallery_page"),
    path("mode/dark/" , views.dark_mode,name="dark_view"),
    path("mode/light/" , views.light_mode,name="light_view"),
    path("colors/", views.colors,name="colors_page"),
    path("map/" , views.map , name="map_page"),
]