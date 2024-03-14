from . import views
from django.urls import path

app_name="main"

urlpatterns=[
    path("",views.home_page,name="home_page"),
      path("/contact",views.contact_Basic,name="contact_Basic"),
       path("/type",views.type_Basic,name="type_Basic"),
       path("/read",views.read_Basic,name="read_Basic"),
       path("/resorce",views.resource_Basic,name="resource_Basic"),
       path("/test",views.test_Basic,name="test_Basic"),
      path('mode/light/', views.light_mode, name='light_mode'),
    path('mode/dark/', views.dark_mode, name='dark_mode'),
    ]