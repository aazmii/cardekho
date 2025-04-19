from rest_framework import serializers

from ..models import CarList
from decimal import Decimal

def alphanumeric (value):
    if not str(value).isalnum: 
        raise serializers.ValidationError("Car name should be alphanumeric")
#Serializer
# class CarSerializer(serializers.Serializer): 
    # id = serializers.IntegerField(read_only=True)
    # carName = serializers.CharField(source = 'car_name', max_length=100)
    # description = serializers.CharField(max_length=200)
    # active = serializers.BooleanField(read_only = True)
    # chassis_number = serializers.CharField(validators = [alphanumeric])
    # price = serializers.DecimalField(max_digits = 9, decimal_places=2)

    # def create(self, validated_data):
    #     return CarList.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.car_name = validated_data.get('car_name', instance.car_name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.chassis_number = validated_data.get('chassis_number', instance.chassis_number)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance
    # MODEL SERIALIZER
class CarSerializer (serializers.ModelSerializer):
    descounted_price = serializers.SerializerMethodField()
    def get_descounted_price(self, obj):
        if obj.price is None: 
            return None
        return obj.price * Decimal (0.9)
    class Meta: 
        model = CarList
        fields = "__all__"

    def validate_price(self, value):
        if value is None:
          raise serializers.ValidationError("Price is required.")
        if value <= 20000.00: 
            raise serializers.ValidationError("Car price must be greater than 20000")
        return value
    def validate(self,data): 
        if data['car_name']== data['description']: 
            raise serializers.ValidationError("Name and description should not be same")
        return data