from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Booking
from restaurants.models import Restaurant
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
        restaurant = Restaurant.objects.get(pk=kwargs["pk"])
        bookings = Booking.objects.filter(restaurants=restaurant)
        
        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "booking_form": BookingForm(),
                "bookings": bookings,
                'restaurant': restaurant,
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
        booking_form = BookingForm(data=request.POST)
        restaurant = Restaurant.objects.get(id=request.POST.get("restaurants"))

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.email = request.user.email
            booking.name = request.user.username
            booking.restaurants = restaurant
            # booking.booking_form = booking_form
            booking_form.save()
            return redirect('/')
        else:
            booking_form = BookingForm()

        return render(
            request, 
            "bookings/booking_detail.html", 
            {
                "restaurant": Restaurant,
                "booking_form": BookingForm()
            }
        )

# def post(self, request, pk, *args, **kwargs):
#         restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
#         review_form = ReviewForm(data=request.POST)
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.email = request.user.email
#             review.name = request.user.username
#             review.restaurants = restaurant
#             review_form.save()
#             return redirect('/')
#         else:
#             review_form = ReviewForm()

#         return render(
#             request, 
#             "restaurants/restaurant_detail.html", 
#             {
#                 'restaurant': Restaurant,
#                 'review': review,
#                 "reviewed": True,
#                 'bookings': Booking,
#                 "review_form": ReviewForm(),
#                 "booking_form": BookingForm()
#             },
#         )

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
    template_name = 'bookings/delete_booking.html'
    success_url = reverse_lazy('booking')


