from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
from django.urls import reverse

# Create your views here.
def welcome_view(request: HttpRequest):
    return render(request, "main/welcome.html")

def home_view(request):
    # Simulate a delay to display the welcome page for a few seconds
    time.sleep(2)  # Adjust the sleep time as needed

    # Render the index.html template
    return render(request, 'main/index.html')

def old_view(request:HttpRequest):
    return render(request,"main/old_football.html")

def now_view(request:HttpRequest):
    return render(request, "main/now_football.html")

def future_view(request:HttpRequest):
    return render(request, "main/future_football.html")

def clubs_view(request:HttpRequest):
    return render(request, "main/saudi_clubs.html")

def dark_mode(request:HttpRequest):
    response = redirect('main:home_view')
    response.set_cookie("dark_mode", "True")
    return response

def light_mode(request:HttpRequest):
    response = redirect('main:home_view')
    response.set_cookie("dark_mode", "False")
    return response
