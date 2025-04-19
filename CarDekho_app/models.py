from django.db import models

# Create your models here.
class CarList(models.Model): 
    car_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=False)
    chassis_number  = models.CharField(max_length = 100, blank = True, null = True)
    price = models.DecimalField(max_digits = 9, decimal_places=2, blank= True, null = True)    