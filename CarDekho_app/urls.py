from django.urls import path 
 

# from views.car_view import car_list_view,car_detail_view
# from views.showroom_view import Showroom_View

from CarDekho_app.views.car_view import car_list_view, car_detail_view
from CarDekho_app.views.showroom_view import Showroom_View, Showroom_Details

 
urlpatterns = [
    path('cars', car_list_view, name='car_list'),
    path ('<int:id>', car_detail_view, name = 'car_detail'),
    path('showrooms',  Showroom_View.as_view(), name='showroom'),
    path('showroom/<int:id>', Showroom_Details.as_view(), name='showroom_detail'),   
]