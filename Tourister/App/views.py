from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_page(request: HttpRequest):

    return render(request,"App/home.html")



def dark_mode_view(requset: HttpRequest):

    response = redirect("App:home_page")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("App:home_page")
    response.set_cookie("mode", "light")
    
     
    return response

def saudi_view(request:HttpRequest):
    return render(request,'App/saudi.html')
def flagday_view(request: HttpRequest):
    return render(request,'App/flagday.html')

def history_view(request: HttpRequest):
    return render(request,"App/history.html")

def conclusion_view(request: HttpRequest):
    return render(request,"App/conclusion.html")

