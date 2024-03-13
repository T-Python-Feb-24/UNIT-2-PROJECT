from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'saudihis/home.html')

def middlestate(request):
    return render(request, 'saudihis/middlestate.html')

def northstate(request):
    return render(request, 'saudihis/northstate.html')

def eaststate(request):
    return render(request, 'saudihis/eaststate.html')

def westestate(request):
    return render(request, 'saudihis/westestate.html')

def southstate(request):
    return render(request, 'saudihis/southstate.html')


def dark_mode_view(requset: HttpRequest):

    response = redirect("saudihis:main")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("saudihis:main")
    response.set_cookie("mode", "light")

    return response
