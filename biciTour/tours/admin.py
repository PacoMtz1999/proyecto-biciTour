from django.contrib import admin
from .models import recorridos
from .models import mensajeContacto 
from .models import registrameRecorrido

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    list_display = ('id','ciudad','fecha','pInicio')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')

admin.site.register(recorridos, AdministrarModelo)

class AdministrarMensajesContacto(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(mensajeContacto, AdministrarMensajesContacto)

class AdministrarRegistrosRecorridos(admin.ModelAdmin):
    list_display = ('id', 'recorrido')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(registrameRecorrido, AdministrarRegistrosRecorridos)