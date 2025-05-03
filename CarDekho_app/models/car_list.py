from django.db import models
from django.forms import ValidationError
from .showroom import ShowroomList

def alphanumeric (value): 
    if not str(value).isalnum():
        raise ValidationError("Car name should be alphanumeric")
    return value
# Create your models here.
class CarList(models.Model): 
    car_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=False)
    chassis_number  = models.CharField(max_length = 100, blank = True, null = True, validators=[alphanumeric])
    price = models.DecimalField(max_digits = 9, decimal_places=2, blank= True, null = True)    
    shworoom = models.ForeignKey(ShowroomList, on_delete = models.CASCADE, related_name = 'Showrooms', null = True)

    def __str__(self):
        return self.car_name