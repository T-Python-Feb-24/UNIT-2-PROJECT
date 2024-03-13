from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):

    return render(request, 'development/home_page.html')



def roshn(request:HttpRequest):

    return render(request, 'development/roshn.html')



def neom(request:HttpRequest):

    return render(request, 'development/neom.html')



def red_sea(request:HttpRequest):

    return render(request, 'development/red_sea.html')



def qiddiya(request:HttpRequest):

    return render(request, 'development/qiddiya.html')


def dark_mode_view(requset: HttpRequest):

    response = redirect("development:home_page")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("development:home_page")
    response.set_cookie("mode", "light")

    return response