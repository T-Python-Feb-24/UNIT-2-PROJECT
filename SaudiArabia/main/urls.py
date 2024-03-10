from . import views
from django.urls import path

app_name = "main"
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path("mode/light/", views.mode_light, name="mode_light"),
    path("mode/dark/", views.mode_dark, name="mode_dark"),
    path('properties/', views.properties_page, name="properties_page"),
    path('about', views.about_page, name="about_page"),
    path('contactus', views.contactus_page, name="contactus_page"),
]
