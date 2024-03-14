from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_view(request:HttpRequest):

    return render(request, "main/index.html")

def island_view(request:HttpRequest):

    return render(request, "main/island.html")

def event_view(request:HttpRequest):

    return render(request, "main/event.html")

def cont_view(request:HttpRequest):

    return render(request, "main/contact.html")

def about_view(request:HttpRequest):

    return render(request, "main/about.html")

def dark_mode_view(request: HttpRequest):

    response=redirect(request.GET.get("next"))
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(request: HttpRequest):

    response=redirect(request.GET.get("next"))
    response.set_cookie("mode", "light")

    return response