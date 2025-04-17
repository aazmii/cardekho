from rest_framework import serializers

from ..models import CarList

class CarSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    carName = serializers.CharField(source = 'car_name', max_length=100)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField(read_only = True)

    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', instance.car_name);
        instance.description = validated_data.get('description', instance.description);
        instance.active = validated_data.get('active', instance.active);
        instance.save()
        return instance