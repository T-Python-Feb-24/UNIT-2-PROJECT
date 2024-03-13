from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):
    return render(request, 'main/home.html')

def region_page(request:HttpRequest):

    return render(request, 'main/regions.html') 

def culture_page(request:HttpRequest):
    return render(request, 'main/culture.html')

def heritage_page(request:HttpRequest):
    return render(request, 'main/heritage.html')

def dark_mode(request:HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "True", max_age=60*60*24*7)

    return response

def light_mode(request:HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "False")

    return response