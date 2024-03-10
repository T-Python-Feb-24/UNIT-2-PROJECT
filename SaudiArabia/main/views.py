from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpRequest


def home_page(request: HttpRequest):

    return render(request, "index.html")


def mode_light(request: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "False")

    return response


def mode_dark(request: HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode", "True")

    return response


def properties_page(request: HttpRequest):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]

    context = {"properties": properties}

    return render(request, "properties.html", context)


def about_page(request: HttpRequest):

    return render(request, "about.html")


def contactus_page(request: HttpRequest):
    return render(request, "contactus.html")
