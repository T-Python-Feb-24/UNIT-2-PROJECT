from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.
def home_page(request:HttpRequest):

    return render(request,'main/index.html')

def neom_page(request:HttpRequest):
      return render(request,"main/neom.html")

def regions_page(request:HttpRequest):
      return render(request,"main/regions.html")

def vision_gools(request:HttpRequest):
      return render(request,'main/vision_gools.html')

def Qiddiya_page(request:HttpRequest):
      return render(request,'main/Qiddiya.html')

def dark_mode(request:HttpRequest):
        response=redirect(request.GET.get("next"))
        response.set_cookie("mode", "dark")
        return response


def light_mode(request:HttpRequest):
      response=redirect(request.GET.get("next"))
      response.set_cookie("mode","light")
      return response

def language_ar(request:HttpRequest):
        response=redirect(request.GET.get("next"))
        response.set_cookie("language","ar")
        return response


def language_en(request:HttpRequest):
      response=redirect(request.GET.get("next"))
      response.set_cookie("language","en")
      return response
