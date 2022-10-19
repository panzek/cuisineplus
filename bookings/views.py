from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy

class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings/booking_detail.html'

    context = {
        'bookings': Booking.objects.all()
    }
    
    # ---- End Self -----
    """
    Get data from forms.py and render in booking_form
    """

    def get(self, request, *args, **kwargs):
        print(self, request, args, kwargs)

        bookings = Booking.objects.all()
        
        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "booking_form": BookingForm(),
                "bookings": bookings,
                }
        )

    # ---- End Self ---

    
    # ---- Akshat -----
    # """
    # Get data from forms.py and render in booking_form
    # """

    # def get(self, request, *args, **kwargs):
    #     print(request.user)

    #     bookings = Booking.objects.filter(user__id=request.user.id)

    #     return render(
    #         request, 
    #         "bookings/booking_detail.html", 
    #         {
    #             "booking_form": BookingForm(),
    #             "bookings": bookings,
    #             }
    #     )

    # ---- End Akshat -----


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

 
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking.html'
    queryset = Booking.objects.all()

    def get_object(self):
        return get_object_or_404('')


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_url = '/'

    def success(request):
        return render(request, '/')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'bookings/confirm_delete.html'
    success_url = reverse_lazy('')


# BIG SELF 
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import generic
# from django.views.generic.edit import UpdateView
# from .models import Booking
# from .forms import BookingForm

# class BookingList(generic.ListView):
#     model = Booking
#     template_name = 'bookings/booking_detail.html'

#     context = {
#         'bookings': Booking.objects.all()
#     }
    
#     """
#     Get data from forms.py and render in booking_form
#     """

#     def get(self, request, *args, **kwargs):

#         bookings = Booking.objects.all()
        
#         return render(
#             request, 
#             "bookings/booking_detail.html", 
#             {
#                 "booking_form": BookingForm(),
#                 "bookings": bookings,
#                 }
#         )


#     """
#     Post data to database 
#     """

#     def post(self, request):
#         if request.method == 'POST':
#             booking_form = BookingForm(request.POST)
#             if booking_form.is_valid():
#                 booking = booking_form.save(commit=False)
#                 booking.booking_form = booking_form
#                 booking.save()
#                 return redirect('bookings/booking_detail.html')
#             else:
#                 booking_form = BookingForm()

#         return render(
#             request, 
#             "bookings/booking_detail.html", 
#             {
#                 "booking_form": BookingForm()
#             }
#         )


# class BookingUpdateView(UpdateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'bookings/edit_booking.html'
#     success_url = '/success/'

#     def success(request):
#         return render(request, 'success.html')

# ---- SMALL self --- 
# class BookingCreateView(CreateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'bookings/booking.html'
#     queryset = Booking.objects.all()

#     def get_object(self):
#         return get_object_or_404('')
   

# class BookingUpdateView(UpdateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'bookings/booking.html'

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Booking, id=id_)
# ---- end SMALL self --- 

# ---- END BIG SELF
