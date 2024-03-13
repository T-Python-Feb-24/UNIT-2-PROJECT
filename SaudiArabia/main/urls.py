from . import views
from django.urls import path

app_name = "main"
urlpatterns = [
    path('', views.home_page, name="home_page"),
    path("mode/light/", views.mode_light, name="mode_light"),
    path("mode/dark/", views.mode_dark, name="mode_dark"),
    path('business-economy/', views.business_economy_page,
         name="business_economy_page"),
    path('national-biotechnology-strategy/',
         views.national_biotechnology_strategy, name="nb_strategy"),
    path('neom/', views.neom_page, name="neom_page"),
    path('oxagon/', views.oxagon_page, name="oxagon_page"),
    path('investment/', views.investment_page, name="investment_page"),
    path('made_in_saudi/', views.made_in_saudi_page, name="made_in_saudi_page"),
    path('contactus', views.contactus_page, name="contactus_page"),
]
