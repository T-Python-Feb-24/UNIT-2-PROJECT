from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.welcome_view, name="welcome_view"),  # Welcome page
    path("home/", views.home_view, name="home_view"),  # Index page
    path("old/football/", views.old_view, name="old_view"),
    path("now/football/", views.now_view, name="now_view"),
    path("future/football/", views.future_view, name="future_view"),
    path("saudi/clubs/", views.clubs_view, name="clubs_view"),
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode"),
]
