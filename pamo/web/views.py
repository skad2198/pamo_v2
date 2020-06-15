from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import vehicle
# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def cars_page(request, pg=1):

    # Each page has 9 requests. That is fixed.
    start = (pg-1) * 6
    end = start + 6

    car_list = vehicle.objects.all()[start:end]
    context = {
        'cars': car_list
    }

    return render(request, 'web/cars.html', context)

def cars_details(request, car_id):
    print(car_id)
    car_detail = vehicle.objects.get(pk=car_id)
    print(car_detail.name)
    context = {
        'car_detail' : car_detail, 
    }
    return render(request,'web/cars_details.html',context)
