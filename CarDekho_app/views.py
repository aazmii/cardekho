from django.shortcuts import render
from .models import CarList
from django.http import JsonResponse
# Create your views here.
def car_list_view(request): 
    cars = CarList.objects.all()
    data = {
        'cars:': list(cars.values())
    }
    return JsonResponse(data)

def car_detail_view(request, id): 
    car = CarList.objects.get(id =id)
    data = {
        'name': car.name,
        'description': car.description,
        'active': car.active,
    }
    return JsonResponse(data)