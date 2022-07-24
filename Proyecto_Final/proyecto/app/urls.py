from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about_me/',views.about_me, name= 'about_me'),


]