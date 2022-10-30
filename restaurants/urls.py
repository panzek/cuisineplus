# from django.urls import path
# from .views import RestaurantList, RestaurantDetail

# urlpatterns = [
#     path(
#         'restaurant_list.html/', 
#         RestaurantList.as_view(), 
#         name='restaurants'
#         ),   

#     path(
#         'restaurant_detail/<pk>', 
#         RestaurantDetail.as_view(), 
#         name='restaurant_detail'
#         ), 
    
#     path(
#         'restaurant_detail.html', 
#         RestaurantList.as_view(), 
#         name='restaurant'
#         ),
# ]


from django.urls import path
from .views import RestaurantList, RestaurantDetail, ReservationList, ReservationUpdateView

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
    
    path(
        'reservation_list.html/', 
        ReservationList.as_view(), 
        name='reservation'
        ),

    path(
        'restaurants/edit_reservation/<pk>', 
        ReservationUpdateView.as_view(), 
        name='edit'
        ),
]