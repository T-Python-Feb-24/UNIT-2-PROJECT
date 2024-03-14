from . import views
from django.urls import path

app_name = 'saudi_arabia'

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('energy/', views.energy_page, name = 'energy_page'),
    path('maining/', views.maining_page, name = 'maining_page'),
    path('industry/', views.industry_page, name = 'industry_page'),
    path('logistics/', views.logistics_page, name = 'logistics_page'),
]