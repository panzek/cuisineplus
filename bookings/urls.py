from django.urls import path
from .views import BookingList, BookingUpdateView
# from bookings.views import edit_booking
# from .views import BookingUpdateView

urlpatterns = [
    path(
        'booking_detail.html/', 
        BookingList.as_view(), 
        name='booking'
        ),

    # path(
    #     'edit_booking.html/', 
    #     views.BookingList.as_view(), 
    #     name='edit_booking'
    #     ),
    
    
    
    # path('edit/<booking_id>', edit_booking, name='edit_booking'),
    path('edit_booking/<booking_id>', BookingUpdateView.as_view(), name='edit'),
    
]