# Class based serializer

from rest_framework import serializers
from ..models.showroom import ShowroomList

class ShowroomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ShowroomList
        fields = "__all__"
