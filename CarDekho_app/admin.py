from django.contrib import admin
from .models.car_list import CarList 
from .models.showroom import ShowroomList
# Register your models here.

admin.site.register(CarList)
admin.site.register(ShowroomList)
