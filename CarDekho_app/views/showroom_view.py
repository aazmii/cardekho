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
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data)
        else: 
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
class Showroom_Details (APIView):
    def get (self,request, id): 
        try: 
            showroom = ShowroomList.objects.get(id =id)
        except ShowroomList.DoesNotExist:
            return Response({'Error': 'Showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)
        

    def put (self, request,id): 
        showroom = ShowroomList.objects.get(id=id)
        serializer = ShowroomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
         showroom = ShowroomList.objects.get(id = id)
         showroom.delete()
         return Response(status = status.HTTP_204_NO_CONTENT)