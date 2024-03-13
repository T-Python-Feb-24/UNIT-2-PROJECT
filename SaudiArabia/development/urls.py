from . import views
from django.urls import path 

app_name = 'development'

urlpatterns = [
    path('', views.home_page , name="home_page"),
    path('development/roshn/', views.roshn , name="roshn"),
    path('development/neom/', views.neom , name="neom"),
    path('development/red_sea/', views.red_sea , name="red_sea"),  
    path('development/qiddiya/', views.qiddiya , name="qiddiya"),
    path('mode/light/', views.light_mode_view , name='Light_mode_view'),
    path('mode/dark/', views.dark_mode_view , name='dark_mode_view'),
]
