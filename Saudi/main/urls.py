from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),
    path("islamic/", views.islamic_view, name="islamic_view"),
    path("capital/", views.capital_view, name="capital_view"),
    path("jeddah/", views.jeddah_view, name="jeddah_view"),
    path("riyadh/", views.riyadh_view, name="riyadh_view"),
]