from django.urls import path
from . import views

urlpatterns = [
    path('booking_detail.html/', views.BookingList.as_view(), name='Booking Detail'),
    path('booking_form.html/', views.BookingList.as_view(), name='Booking Detail'),
]