from django.urls import path
from.import views 

app_name='main'

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('Distance/',views.distance_page,name="distance_page"),
    path('Currency/',views.currency_exchange,name="currency_exchange"),
    path('Weather/',views.weather_informations,name="weather_informations"),
    path('Riyadh/',views.riyadh_page,name="riyadh_page"),
    path('Jeddah/',views.jeddah_page,name="jeddah_page"),
    path('Al-ula/',views.alula_page,name="alula_page"),
    path('Abha/',views.abha_page,name="abha_page"),
    path("mode/light/",views.light_mode_view,name="light_mode_view"),
    path("mode/dark/",views.dark_mode_view,name="dark_mode_view"),
]
