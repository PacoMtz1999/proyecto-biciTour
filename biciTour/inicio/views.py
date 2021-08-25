from django.shortcuts import redirect, render
""" from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages """


# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def recoproxi(request):
    return render(request,"inicio/recoproxi.html")

def recoreali(request):
    return render(request,"inicio/recoreali.html")

def nosotros(request):
    return render(request,"inicio/nosotros.html")

def contacto(request):
    return render(request,"inicio/contacto.html")

def login(request):
    return render(request,"inicio/login.html")

