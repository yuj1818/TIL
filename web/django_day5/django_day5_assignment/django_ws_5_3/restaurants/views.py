from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = list(Restaurant.objects.all().order_by('name'))
    
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

    new_pk = Restaurant.objects.last().pk

    return redirect('detail', restaurant_pk=new_pk)

def detail(request, restaurant_pk):
    restaurant_info = Restaurant.objects.get(pk=restaurant_pk)

    context = {
        'info': restaurant_info
    }

    return render(request, 'restaurants/detail.html', context)

def edit(request, restaurant_pk):
    restaurant_info = Restaurant.objects.get(pk=restaurant_pk)

    context = {
        'info': restaurant_info
    }

    return render(request, 'restaurants/edit.html', context)

def update(request, restaurant_pk):
    name = request.POST['name']
    description = request.POST['description']
    address = request.POST['address']
    phone_number = request.POST['phone_number']

    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.name = name
    restaurant.description = description
    restaurant.address = address
    restaurant.phone_number = phone_number
    restaurant.save()

    return redirect('detail', restaurant_pk=restaurant.pk)

def delete(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant.delete()
    return redirect('index')