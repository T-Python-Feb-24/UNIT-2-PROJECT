from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

def home_page(request:HttpRequest):

    return render(request, "CultureHeritage/home_page.html")

def dark_mode(requset: HttpRequest):

    response = redirect("CultureHeritage:home_page")
    response.set_cookie("mode", "dark")

    return response


def light_mode(requset: HttpRequest):

    response = redirect("CultureHeritage:home_page")
    response.set_cookie("mode", "light")

    return response

def culture(request:HttpRequest):

    return render(request, "CultureHeritage/culture.html")

def heritage(request:HttpRequest):

    return render(request, "CultureHeritage/heritage.html")

def vision(request:HttpRequest):

    return render(request, "CultureHeritage/vision.html")

def saudi(request:HttpRequest):

    return render(request, "CultureHeritage/saudi.html")




