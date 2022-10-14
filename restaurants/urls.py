from django.urls import path
from . import views

urlpatterns = [
    path(
        'restaurant_list.html/', 
        views.RestaurantList.as_view(), 
        name='restaurants'
        ),
    
]