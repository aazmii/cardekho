from django.urls import path 
from . import views 

urlpatterns = [
    path('list', views.car_list_view, name='car_list'),
    path ('<int:id>', views.car_detail_view, name = 'car_detail'),
    # path ('detail/<int:id>', views.car_detail_view, name='car_detail')
   
]