from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import vehicle
from django.db.models import Q
from django.http import HttpResponse, request
from django.core import serializers
# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def cars_page(request, pg=1):

    # Each page has 9 requests. That is fixed.
    start = (pg-1) * 9
    end = start + 9

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

def search_cars(request):
    print('I am here ')
    if request.GET:
        search_term = request.GET['search']
        #search_term = search
        print('I am here in IF ')
        search_results = vehicle.objects.filter(
            Q(name__icontains=search_term) |
            Q(brand__icontains=search_term) |
            Q(description__icontains=search_term) | 
            Q(vehicle_type__icontains=search_term) 
        )
        error_message="Here's your search result for : " + search_term
        context = {
        'error_message':error_message,
        'search_term':search_term,
        'cars':search_results
        }
        return render(request, 'web/cars.html', context)
    else:
        car_list = vehicle.objects.all()
        print('I am here in else')
        error_message='Nothing realted to your search'
        context = {
            'error_message' : error_message,
            'cars': car_list,
        }
        return render(request, 'web/cars.html', context)