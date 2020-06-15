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
