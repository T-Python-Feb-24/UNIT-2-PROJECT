from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

#صفحه الهوم 
def home_view(request:HttpRequest):
    return render(request,"main/home.html")
#صفحة القصة
def main_view(request:HttpRequest):
    return render(request, "main/home_page.html")

#المنطقة الوسطى 
def center_view(request:HttpRequest):
    food = [
        {"title" : "Al-Jareesh", "image" : "jresh.jpeg"},
        {"title" : "Al-Gorsan", "image" : "gorsan.jpeg"},
        {"title" : "Al-Mataziz" ,"image" : "mataziz.jpeg"},
    ]
    site=[
       {"title" : "AL-Masmak palace","image" : "masmak.jpeg"},
        {"title" : "Ushaigar heritage village", "image" : "usheger.jpeg"},
        {"title" : "Al-Murabba historical palace", "image" : "mrba.jpeg"},
    ]
    man =[
       {"title" : "Traditional attire for Men", "image" : "manc.jpeg"},
        {"title" : "Traditional attire for Men" ,"image" : "mancc.jpeg"},
    ]
    woman =[
        {"title" : "Traditional attire for Women", "image" : "womanccc.jpeg"},
            {"title" : "Traditional attire for Women", "image" : "womancc.jpeg"},
        ]
    child =[
       {"title" : "Traditional attire for Boys", "image" : "childccc.jpeg"},
        {"title" : "Traditional attire for Girls" ,"image" : "childcc.jpeg"},
    ]


    context = {
        "food" : food,
        "site": site,
        "man":man,
        "woman":woman,
        "child":child,
    }

    return render(request, "main/center.html",context)

#المنطقة الجنوبية
def south_view(request:HttpRequest):
    foodSouth = [
        {"title" : "Al-Haneth", "image" : "haneth.jpeg"},
        {"title" : "Al-Ssedah", "image" : "asydah.jpeg"},
        {"title" : "Al-Ragsh", "image" : "ragash.jpeg"},
    ]
    siteSouth=[
       {"title" : "Hisn Al-Sharif", "image" : "sharef.jpeg"},
        {"title" : "Rijal Al-Ma Village", "image" : "rijal.jpeg"},
        {"title" : "Shada Palace", "image" : "shada.jpeg"},
    ]
    manwomanSouth =[
       {"title" : "Traditional attire for Men", "image" : "mans.jpg"},
        {"title" : "Traditional attire for Momen", "image" : "womans.jpg"},
    ]
   
    childSouth =[
       {"title" : "Traditional attire for boys", "image" : "childs.jpg"},
        {"title" : "Traditional attire for girls", "image" : "childsss.jpeg"},
    ]


    context = {
        "foodSouth" : foodSouth,
        "siteSouth": siteSouth,
        "manwomanSouth":manwomanSouth,
        "childSouth":childSouth,
    }
    return render(request,"main/south.html",context)
#المنطقةالشرقية
def east_view(request:HttpRequest):
    foodEast = [
        {"title" : "Al-Ahsa rice", "image" : "rz.jpeg"},
        {"title" : "Red bread with dates", "image" : "kobzz.jpeg"},
        {"title" : "Hares", "image" : "hres.jpeg"},
    ]
    siteEast=[
       {"title" : "AL-Qaysariyah ", "image" : "gys.jpeg"},
        {"title" : "Tarout Castle", "image" : "tarut.jpeg"},
        
    ]
    manwomanEast =[
       {"title" : "Traditional attire for Men", "image" : "mane.jpeg"},
        {"title" : "Traditional attire for Women", "image" : "womane.jpeg"},
    ]
  
       
    childEast =[
       {"title" : "Traditional attire for boys", "image" : "childee.jpeg"},
        {"title" : "Traditional attire for girls", "image" : "childe.jpeg"},
    ]


    context = {
        "foodEast" : foodEast,
        "siteEast": siteEast,
        "manwomanEast":manwomanEast,
        "childEast":childEast,
    }

    return render(request,"main/east.html",context)
#المنطقة الغربية
def west_view(request:HttpRequest):
    foodWest = [
        {"title" : "Arekah", "image" : "arekh.jpeg"},
        {"title" : "Debiaza", "image" : "debyazh.jpeg"},
        {"title" : "Mento", "image" : "mnto.jpeg"},
    ]
    siteWest=[
       {"title" : "King Abdulaziz Palace", "image" : "abdulaziz.jpeg"},
        {"title" : "The Railroad Museum", "image" : "road.jpeg"},
       
    ]
    manWest =[
       {"title" : "Traditional attire for Men", "image" : "manw.jpeg"},
        {"title" : "Traditional attire for Men", "image" : "manww.jpeg"},
    ]
    womanWest=[
        {"title" : "Traditional attire for women", "image" : "womanw.jpeg"},
            {"title" : "Traditional attire for women", "image" : "womanww.jpeg"},
        ]
    childWest=[
       {"title" : "Traditional attire for boys", "image" : "childw.jpeg"},
        {"title" : "Traditional attire for girls", "image" : "childww.jpeg"},
    ]


    context = {
        "foodWest" : foodWest,
        "siteWest": siteWest,
        "manWest":manWest,
        "womanWest":womanWest,
        "childWest":childWest,
    }

    return render(request,"main/west.html",context)
#المنطقة الشمالية
def north_view(request:HttpRequest):
    foodNorth = [
        {"title" : "Al-Mansaf", "image" : "mansaf.jpeg"},
        {"title" : "Al-Kleija", "image" : "klygah.jpeg"},
        
    ]
    siteNorth=[
        {"title" : "The historic Tabuk Castle", "image" : "tabuk.jpeg"},
        {"title" : "AL-Qunun Chamber", "image" : "ganon.jpeg"},

       
    ]
    manwomanNorth =[
       {"title" : "Traditional attire for Men", "image" : "mann.jpeg"},
        {"title" : "Traditional attire for woman", "image" : "womann.jpeg"},
    ]
   
    childNorth=[
       {"title" : "Traditional attire for boys", "image" : "childn.jpeg"},
        {"title" : "Traditional attire for girls", "image" : "childnn.jpeg"},
    ]


    context = {
        "foodNorth" : foodNorth,
        "siteNorth": siteNorth,
        "manwomanNorth":manwomanNorth,
        "childNorth":childNorth,
    }


    return render(request,"main/north.html",context)

def dark_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_mode_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response