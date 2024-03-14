from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

#Create your views here.
def home_view(request:HttpRequest):
    return render(request, "main/index.html")

def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

def islamic_view(request: HttpRequest):
    return render(request, "main/islamic.html")

def riyadh_view(request: HttpRequest):
    return render(request, "main/riyadh.html")

def jeddah_view(request: HttpRequest):
    return render(request, "main/jeddah.html")

def capital_view(request: HttpRequest):
    return render(request, "main/capital.html")
