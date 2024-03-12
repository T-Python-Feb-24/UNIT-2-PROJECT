from django.shortcuts import render

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
