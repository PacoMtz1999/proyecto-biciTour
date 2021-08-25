from django import forms
from .models import mensajeContacto
from .models import registrameRecorrido

class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model = mensajeContacto
        fields = ['nombre','email','asunto','mensaje']

class RegistroRecorridoForm(forms.ModelForm):
    class Meta:
        model = registrameRecorrido
        fields = ['nombre','email','recorrido','telefono','nPersonas']