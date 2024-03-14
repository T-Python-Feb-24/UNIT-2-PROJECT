from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest):


    return render(request, "main/index.html")

def museums_view(request: HttpRequest):
     return render(request, "main/museums.html")
 
def about_view(request: HttpRequest):
     return render(request, "main/about.html")

def contact_view(request: HttpRequest):

    return render(request, "main/contact.html")



def dark_mode_view(requset: HttpRequest):

    response=redirect(requset.GET.get("next"))

    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response=redirect(requset.GET.get("next"))
    response.set_cookie("mode", "light")

    return response

def destinations_view(request: HttpRequest):
    destinations = [
        {"title": "Abha", "image": "184127.avif", "description": "Scenic park known for its lush greenery and stunning mountain landscapes."},
        {"title": "Farasan Islands", "image": "farasan_islands.jpg", "description": "Group of islands renowned for their coral reefs, marine life, and pristine beaches."},
        {"title": "Najran: Ancient City", "image": "homeback.jpeg", "description": "Historic city with traditional architecture and rich cultural heritage."},
        {"title": "Al Baha: Mountain Resort", "image": "al_baha.jpg", "description": "Mountainous region offering hiking trails, cool climate, and beautiful scenery."},
        {"title": "Abha: Southern Gateway", "image": "abha.jpg", "description": "City known for its mild climate, parks, and traditional souks."},
    ]

    return render(request, "main/destinations.html", {"destinations": destinations})

# def najranـview(requset: HttpRequest):

#     return render(requset, "main/najran.html")
    
def najran_view(request):
    
    return render(request, 'main/najran_detail.html')
    
def asir_view(request):
    return render(request, 'main/asir.html')

def Jizan_view(request):
    return render(request, 'main/Jizan.html')

def baha_view(request):
    return render(request, 'main/baha.html')

