# from CarDekho.CarDekho_app import models
from django.db import models


class ShowroomList(models.Model):
    showroom_name = models.CharField(max_length=100)
    showroom_address = models.CharField(max_length=100)
    showroom_contact = models.CharField(max_length=100)

    def __str__(self):
        return self.showroom_name