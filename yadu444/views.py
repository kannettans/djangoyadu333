from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("im yadu")


# def home1(request):
#     x= [1,2,3,]
#     return render(request,"home.html",{"data":x})

def home(request):
    return render (request , "home.html")

def register(request):
    return render ( request , "register.html" )

def log(request):
    return render ( request , "log.html" )

