from django.shortcuts import render
from .forms import MensajeContactoForm
from .forms import RegistroRecorridoForm
from .models import recorridos
from .models import registrameRecorrido

# Create your views here.

def contacto(request):
    return render(request,"tour/contacto.html")

def registrarMensajeContacto(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"tour/contacto.html")
    form = MensajeContactoForm()
    return render(request,"tour/contacto.html",{'form':form})


def registroRecorrido(request):
    return render(request,"tour/formRegistroRecorrido.html")

def registrarRecorridoSelec(request):
    if request.method == 'POST':
        form = RegistroRecorridoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"tour/formRegistroRecorrido.html")
    form = RegistroRecorridoForm()
    return render(request,"tour/formRegistroRecorrido.html",{'form':form})

def consultarRecorridosProximos(request):
    recorridosPro = recorridos.objects.all()
    return render(request,"tour/proximosRecorridos.html",{'recorridosPro':recorridosPro})

def proximosRecorridos(request):
    recorridosPro = recorridos.objects.all()
    return render(request,"tour/proximosRecorridos.html",{'recorridosPro':recorridosPro})

def recorridosRealizados(request):
    recorridosRea = registrameRecorrido.objects.all()
    return render(request,"tour/recorridosRealizados.html",{'recorridosRea':recorridosRea})
