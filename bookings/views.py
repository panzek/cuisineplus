from django.shortcuts import render
from django.views import generic
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    # queryset = Booking.objects.filter(status=1).order_by('-created_on')
    template_name = 'bookings/booking_detail.html'


