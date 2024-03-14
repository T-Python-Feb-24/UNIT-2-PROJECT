from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request:HttpRequest):
    
    return render(request, 'saudi_arabia/home_page.html')

def energy_page(request:HttpRequest):
    
    return render(request, 'saudi_arabia/energy_page.html')


def maining_page(request:HttpRequest):
    
    return render(request, 'saudi_arabia/maining_page.html')

def industry_page(request:HttpRequest):
    
    return render(request, 'saudi_arabia/industry_page.html')

def logistics_page(request:HttpRequest):
    
    return render(request, 'saudi_arabia/logistics_page.html')