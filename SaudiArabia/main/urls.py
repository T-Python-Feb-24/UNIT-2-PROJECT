from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("island/", views.island_view, name="island_view"),
    path("contact/", views.cont_view, name="cont_view"),
    path("about/", views.about_view, name="about_view"),
    path("event/", views.event_view, name="event_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),
]