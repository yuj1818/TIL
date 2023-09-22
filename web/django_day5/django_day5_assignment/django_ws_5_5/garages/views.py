from django.shortcuts import render, redirect
from .models import Garage

# Create your views here.
def index(request):
    data = Garage.objects.all()
    context = {
        'garages': data
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage(location=location,capacity=capacity,is_parking_avaliable=is_parking_avaliable,opening_time=opening_time,closing_time=closing_time)
    garage.save()
    return redirect('garages:index')

def edit(request, garage_pk):
    data = Garage.objects.get(pk=garage_pk)
    context = {
        'garage': data,
        'opening_time': data.opening_time.strftime("%H:%M"),
        'closing_time': data.closing_time.strftime("%H:%M"),
    }
    return render(request, 'garages/edit.html', context)

def update(request, garage_pk):
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    is_parking_avaliable = request.POST.get('is_parking_avaliable')
    opening_time = request.POST.get('opening_time')
    closing_time = request.POST.get('closing_time')

    garage = Garage.objects.get(pk=garage_pk)
    garage.location = location
    garage.capacity = capacity
    garage.is_parking_avaliable = is_parking_avaliable
    garage.opening_time = opening_time
    garage.closing_time = closing_time
    garage.save()
    return redirect('garages:index')

def delete(request, garage_pk):
    garage = Garage.objects.get(pk=garage_pk)
    garage.delete()
    return redirect('garages:index')