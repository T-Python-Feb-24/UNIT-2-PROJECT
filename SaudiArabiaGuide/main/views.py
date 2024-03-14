from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

from .helpers import distanceKm


# Create your views here.

def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')


def distance_page(request:HttpRequest):
    distance = None
    
    if request.method == "POST":
        fromCity = request.POST["fromCity"]
        toCity = request.POST["toCity"]
        distance = distanceKm(fromCity, toCity)
        if distance is not None:
            distance = round(distance,2)
            
    print(distance) 
    return render(request,'main/distance.html', {"distance" : distance})

def currency_exchange(request:HttpRequest):
    return render(request,'main/currency.html')

def weather_informations(request:HttpRequest):
    return render(request,'main/weather.html')

def riyadh_page(request:HttpRequest):
    return render(request,'main/Riyadh.html')

def jeddah_page(request:HttpRequest):
    return render(request,'main/Jeddah.html')

def alula_page(request:HttpRequest):
    return render(request,'main/Al-ula.html')

def abha_page(request:HttpRequest):
    return render (request, 'main/Abha.html')


def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light")

    return response


