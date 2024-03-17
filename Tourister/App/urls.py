from . import views
from django.urls import path

app_name ="App"

urlpatterns=[ 
    path("",views.home_page,name ="home_page"),
    path("flagday/", views.flagday_view, name="flagday_view"),
    path("history/", views.history_view, name="history_view"),
    path("saudi/", views.saudi_view, name="saudi_view"),
    path("conclusion/", views.conclusion_view, name="conclusion_view"),
    # path("mode/light/", views.light_mode_view, name="light_mode_view"),

]
