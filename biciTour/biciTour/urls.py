"""biciTour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from tours import views as views_tours
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name="Principal"),
    path('recoproxi/',views_tours.consultarRecorridosProximos,name="Recoproxi"),
    path('recoreali/',views_tours.recorridosRealizados,name="Recoreali"),
    path('nosotros/',views.nosotros,name="Nosotros"),
    path('contacto/',views_tours.contacto,name="Contacto"),
    path('login/',views.login,name="Login"),
    path('RegistrarComentario/',views_tours.registrarMensajeContacto,name="RegistrarComentario"),
    path('registroRecorrido/',views_tours.registroRecorrido,name="registroRecorrido"),
    path('RegistrarRecorrido/',views_tours.registrarRecorridoSelec,name="RegistrarRecorrido"),
]





if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)