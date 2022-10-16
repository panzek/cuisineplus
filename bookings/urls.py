from django.urls import path
from .views import BookingList, BookingUpdateView, BookingCreateView

urlpatterns = [
    path(
        'bookings/booking_detail.html', 
        BookingList.as_view(), 
        name='bookings'
        ),

    # --- self ---
    path(
        'booking.html', 
        BookingCreateView.as_view(success_url="booking.html"), 
        name='booking_create'
        ),
    # --- self end ----

    path(
        'list', 
        BookingList.as_view(), 
        name='booking'
        ),
    
    
    path(
        'edit_booking/<pk>', 
        BookingUpdateView.as_view(), 
        name='edit'
        ),
    
]