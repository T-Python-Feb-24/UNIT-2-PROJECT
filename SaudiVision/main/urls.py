from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("",views.home_page,name="home_page"),
    path("mode/dark",views.dark_mode,name="dark_mode"),
    path("mode/light",views.light_mode, name="light_mode"),
    path("language/ar",views.language_ar,name="language_ar"),
    path("language/en",views.language_en, name="language_en"),
    path("regions/",views.regions_page,name="regions.html"),
    path("2030_gools/",views.vision_gools,name="vision_gools"),
    path("neom/",views.neom_page,name="neom.html"),
    path('Qiddiya/',views.Qiddiya_page,name="Qiddiya.html"),

]