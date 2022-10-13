from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect

class BookingList(generic.ListView):
    model = Booking
    # queryset = Booking.objects.order_by('-created_on')
    template_name = 'bookings/booking_detail.html'

    context = {
        'bookings': Booking.objects.all()
    }
    
    """
    Get data from forms.py and render in booking_form
    """

    def get(self, request, **kwargs):

        # booking_form = get_object_or_404()
        
        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "booking_form": BookingForm()
                }
        )


    """
    Post data to database 
    """

    def post_booking(self, request):

        # if request.method == 'POST':
        #     form = BookingForm(request.POST)
        #     if form.is_valid():
        #         return HttpResponseRedirect('bookings/booking_detail.html')
        #     else:
        #         form = BookingForm()

        # return render(
        #     request, 
        #     "bookings/booking_detail.html", 
        #     {
        #         "form" : form
        #         }
        # )

        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                return redirect('get')
            
        booking_form = BookingForm()
        context = {
                "booking_form": booking_form
            }

        return render(request, "booking_detail.html", context)


        # booking_form = get_object_or_404()
        # if request.method == 'POST':
        #     booking_form = BookingForm(request.POST)
        #     if booking_form.is_valid():
        #         booking = booking_form.save(commit=False)
        #         booking.booking_form = booking_form
        #         booking.save()
        #     else:
        #         booking_form = BookingForm()

        # return render(
        #     request, 
        #     "booking_detail.html", 
        #     {
        #         "booking_form": BookingForm()
        #     }
        # )


