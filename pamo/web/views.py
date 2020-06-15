from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import vehicle
from django.db.models import Q
from django.http import HttpResponse, request
from django.core import serializers
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def cars_page(request):
    #print('I am here ')
    if request.POST:
        search_term = request.POST['search']
        #search_term = search
        #print('I am here in IF ')
        # print(search_term)
        search_results = vehicle.objects.filter(
            Q(name__icontains=search_term) |
            Q(brand__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(vehicle_type__icontains=search_term)
        )

        paginator = Paginator(search_results, 9)  # Show 9 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        error_message = "Here's your search result for : " + search_term

        context = {
            'error_message': error_message,
            'search_term': search_term,
            'page_obj': page_obj,
        }
        return render(request, 'web/cars.html', context)
    else:
        vehicle_list = vehicle.objects.all()
        paginator = Paginator(vehicle_list, 9)  # Show 9 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        #car_list = vehicle.objects.all()
        #print('I am here in else')
        error_message = ''
        context = {
            'error_message': error_message,
            'page_obj': page_obj,
        }
        return render(request, 'web/cars.html', context)
 
def cars_details(request, car_id):
    print(car_id)
    car_detail = vehicle.objects.get(pk=car_id)
    print(car_detail.name)
    context = {
        'car_detail' : car_detail, 
    }
    return render(request, 'web/cars_details.html', context)
