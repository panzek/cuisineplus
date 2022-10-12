from urllib import request
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
from django.http import HttpRequest

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-created_on')
    template_name = 'bookings/booking_detail.html'

    context = {
        'bookings': Booking.objects.all()
    }

    def get_booking_form(self, **kwargs):
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form.save()
            else:
                booking_form = BookingForm()

        return render(request, "booking/booking_form.html", context={'booking_form': booking_form})


