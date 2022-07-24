from django.urls import path
from Historia import views

urlpatterns = [
    path('Formulario',views.historia, name='Formulario')


]