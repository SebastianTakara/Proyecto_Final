from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about_me(request):
    return render(request, "app/about_me.html")