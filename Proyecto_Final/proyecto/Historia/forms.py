from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioHistorias(forms.Form):
    titulo= forms.CharField(max_length=100)
    subtitulo= forms.CharField(max_length=200)
    cuerpo= forms.CharField(max_length=500)
    autor= forms.CharField(max_length=80)
    fecha= forms.CharField(max_length=10)