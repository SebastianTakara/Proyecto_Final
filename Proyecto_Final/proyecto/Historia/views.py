from django.shortcuts import render
from Historia.forms import FormularioHistorias
from Historia.models import Historias
# Create your views here.
def historia(request):

      if request.method == 'POST':

            miFormulario = FormularioHistorias(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  historia = Historias (titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo= informacion['cuerpo'],autor= informacion['autor'], fecha= informacion['fecha']) 

                  historia.save()

                  return render(request, "app/home.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= FormularioHistorias() #Formulario vacio para construir el html

      return render(request, "Historia/FormularioHistorias.html", {"miFormulario":miFormulario})