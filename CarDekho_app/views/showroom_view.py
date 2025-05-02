from rest_framework.response import Response
from CarDekho_app.models.showroom import ShowroomList
from CarDekho_app.serializers.showroom_serializer import ShowroomSerializer
from rest_framework.views import APIView
from rest_framework import status
#Class based View 
class Showroom_View (APIView): 
    def get(self, request): 
        showroom = ShowroomList.objects.all()
        serializer = ShowroomSerializer (showroom, many = True)
        return Response(serializer.data)
    def post (self,request):
        serializer = ShowroomSerializer(data = request.data)
        if(serializer.is_validd()):
             serializer.save()
             return Response(serializer.data)
        else: 
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)