from . import views
from django.urls import path

app_name = "CultureHeritage"

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("CultureHeritage/saudi/",views.saudi,name='saudi'),
    path("CultureHeritage/vision/",views.vision,name='vision'),
    path("CultureHeritage/culture/",views.culture,name='culture'),
    path("CultureHeritage/heritage/",views.heritage,name='heritage'),
    path("mode/dark/",views.dark_mode,name='dark-mode'),
     path("mode/light/",views.light_mode,name='light-mode'),
        
    
]