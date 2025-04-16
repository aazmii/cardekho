from rest_framework import serializers 

class CarSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    carName = serializers.CharField(source = 'car_name', max_length=100)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField(read_only = True)