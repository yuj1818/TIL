from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = list(Restaurant.objects.values())
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    name = request.POST['name']
    description = request.POST['description']
    address = request.POST['address']
    phone_number = request.POST['phone_number']

    Restaurant.objects.create(name=name, description=description, address=address, phone_number=phone_number)

    return redirect('index')