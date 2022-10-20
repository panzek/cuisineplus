from django.urls import path
from .views import RestaurantList, RestaurantDetail

urlpatterns = [
    path(
        'restaurant_list.html/', 
        RestaurantList.as_view(), 
        name='restaurants'
        ),   

    path(
        'restaurant_detail/<pk>', 
        RestaurantDetail.as_view(), 
        name='restaurant_detail'
        ), 
    
    path(
        'restaurant_detail.html', 
        RestaurantList.as_view(), 
        name='restaurant'
        ),
]