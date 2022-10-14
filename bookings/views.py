from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import Booking
from .forms import BookingForm

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

    def get(self, request, *args, **kwargs):

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

    def post(self, request):

        # booking_form = get_object_or_404()
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.booking_form = booking_form
                booking.save()
                return redirect('/')
            else:
                booking_form = BookingForm()

        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "booking_form": BookingForm()
            }
        )

    # def edit_booking(request, booking_id):
    #     booking = get_object_or_404(Booking, id=booking_id)
    #     context = {
    #         "booking_form": BookingForm(instance=Booking)
    #     } 

    #     return render(request, "bookings/edit_booking.html", context),


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_url = '/success/'

    def success(request):
        return render(request, 'success.html')

