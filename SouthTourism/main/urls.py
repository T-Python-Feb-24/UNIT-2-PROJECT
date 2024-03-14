from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('destinations/', views.destinations_view, name='destinations_view'),
    path('museums/', views.museums_view, name='museums_view'),
    path("about/", views.about_view, name="about_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),
    path('najran/', views.najran_view, name='najran_view'),
    path('asir/', views.asir_view, name='asir_view'),
    path('Jizan/', views.Jizan_view, name='Jizan_view'),
    path('baha/', views.baha_view, name='baha_view'),
]