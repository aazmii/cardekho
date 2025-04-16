from django.shortcuts import render
from .models import CarList
from django.http import JsonResponse
from .api.serializer import CarSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# # Create your views here.
# def car_list_view(request): 
#     cars = CarList.objects.all()
#     data = {
#         'cars:': list(cars.values())
#     }
#     return JsonResponse(data)

# def car_detail_view(request, id): 
#     car = CarList.objects.get(id =id)
#     data = {
#         'name': car.name,
#         'description': car.description,
#         'active': car.active,
#     }
#     return JsonResponse(data)

@api_view()
def car_list_view(request): 
    cars = CarList.objects.all()
    serializer = CarSerializer (cars, many = True)
    return Response(serializer.data)

@api_view() 
def car_detail_view(request, id):
    car = CarList.objects.get(id = id)
    serializer = CarSerializer(car)
    return Response(serializer.data)