from django.shortcuts import render
from django.views import generic
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    # queryset = Booking.objects.filter(status=1).order_by('-created_on')
    template_name = 'bookings/booking_detail.html'
    # a template location: /path/to/project/bookings/templates/bookings/booking_detail.html

    context = {
        'bookings': Booking.objects.all()
    }

    # def get_context_data(self, **kwargs):
    #     context = super(BookingList, self).get_context_data(**kwargs)
    #     return context


