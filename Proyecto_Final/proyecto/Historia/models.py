from pyexpat import model
from django.db import models

# Create your models here.
class Historias(models.Model):
    titulo= models.CharField(max_length=100)
    subtitulo= models.CharField(max_length=200)
    cuerpo= models.CharField(max_length=500)
    autor= models.CharField(max_length=80)
    fecha= models.CharField(max_length=10)

