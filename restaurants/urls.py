from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (MenuList, ReservationDeleteView, ReservationList,
                    ReservationUpdateView, RestaurantDetail, RestaurantLike,
                    RestaurantList)

urlpatterns = [
    path(
        'restaurant_list.html/',
        RestaurantList.as_view(),
        name='restaurants'
        ),

    path(
        'restaurant_detail/<pk>',
        login_required(RestaurantDetail.as_view()), name='restaurant_detail'
        ),

    path(
        'restaurant_detail.html',
        RestaurantList.as_view(),
        name='restaurant'
        ),

        path(
        'like/<pk>',
        RestaurantLike.as_view(),
        name="restaurant_like"
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

    path(
        'delete_reservation/<pk>',
        ReservationDeleteView.as_view(),
        name='delete'
        ),

    path(
        'menu_list.html/',
        MenuList.as_view(),
        name='menu'
        ),
]