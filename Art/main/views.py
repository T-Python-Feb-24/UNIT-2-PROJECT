from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.


def home(request:HttpRequest):
    return render(request,"main/home.html")


def about_us(request:HttpRequest):
    return render(request,"main/about_us.html")


def gallery(request:HttpRequest):
    return render (request,"main/gallery.html" )



def dark_mode(request: HttpRequest):
  response = redirect("main:home_page")
  response.set_cookie("modedark", "True", max_age=60*60*24*7)
  return response

def light_mode(request: HttpRequest):
  response = redirect("main:home_page")
  response.set_cookie("modedark", "False", max_age=60*60*24*7)
  return response



def colors(request:HttpRequest):
    return render (request,"main/colors.html" )


def map(request:HttpRequest):
    return render (request,"main/map.html" )