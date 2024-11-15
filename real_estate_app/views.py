from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'real_estate_app/home.html')
