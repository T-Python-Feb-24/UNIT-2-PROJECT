from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('Regions/', views.region_page, name='region_page'),
    
    path('Culture/', views.culture_page, name='culture_page'),
    path('Heritage/', views.heritage_page, name='heritage_page'),

    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode"),  
]