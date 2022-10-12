from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
from django.views import View

class BookingList(generic.ListView):
    model = Booking
    # queryset = Booking.objects.order_by('-created_on')
    template_name = 'bookings/booking_detail.html'

    context = {
        'bookings': Booking.objects.all()
    }
    

    def get(self, request, **kwargs):

        # booking_form = get_object_or_404()
        
        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "booking_form": BookingForm()
                }
        )




# class BookingFormView(View):
    """
    Get data from forms.py and render in booking_form
    """

    def get_booking_form(self, request):

        # booking_form = get_object_or_404()
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.booking_form = booking_form
                booking.save()
            else:
                booking_form = BookingForm

        return render(
            request, 
            "bookings/booking_form.html", 
            {
                "booking_form" : BookingForm()
                }
        )


