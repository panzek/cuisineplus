from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import UpdateView
from restaurants.models import Restaurant, Review, Reservation
from .forms import ReviewForm, ReservationForm
from bookings.forms import BookingForm
from bookings.models import Booking

class RestaurantList(generic.ListView):
    model = Restaurant
    queryset: Restaurant.objects.all()
    template_name = 'restaurants/restaurant_list.html'
    pagination = 8


class RestaurantDetail(generic.DetailView):
    
    model = Restaurant
    
    def get(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.get(pk=kwargs["pk"])
        reviews = Review.objects.filter(restaurants=restaurant)
        reservations = Reservation.objects.filter(restaurants=restaurant)

        context = {
            'restaurant': restaurant,
            'reviews': reviews,
            'reservations': reservations,
            "reviewed": False,
            'bookings': Booking,
            "review_form": ReviewForm(),
            "reservation_form": ReservationForm(),
            "booking_form": BookingForm(),
        }

        return render(
            request, 
            'restaurants/restaurant_detail.html',
            context)
    
    """
    Post data to database 
    """

    def post(self, request, pk, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.email = request.user.email
            review.name = request.user.username
            review.restaurants = restaurant
            review_form.save()
            return redirect('/')
        else:
            review_form = ReviewForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                'restaurant': Restaurant,
                # --- 'review': review, ---
                "reviewed": True,
                # 'bookings': Booking,
                "review_form": ReviewForm(),
            },
        )
    
    # --- Reservation view ---
    def post(self, request, pk, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.email = request.user.email
            reservation.name = request.user.username
            reservation.restaurants = restaurant
            reservation_form.save()
            return redirect('/')
        else:
            reservation_form = ReservationForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                'restaurant': Restaurant,
                "reservation_form": ReservationForm(),
            },
        )



class ReservationList(generic.ListView):
    model = Reservation
    queryset: Restaurant.objects.all()
    template_name = 'restaurants/reservation_list.html'
    pagination = 8

    # --- Reservation view ---
    def post(self, request, pk, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.email = request.user.email
            reservation.name = request.user.username
            reservation.restaurants = restaurant
            reservation_form.save()
            return redirect('/')
        else:
            reservation_form = ReservationForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                'restaurant': Restaurant,
                'reservation': reservation,
                "reservation_form": ReservationForm(),
            },
        )
    

    

#  --- Reservation Update ---

class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurants/edit_reservation.html'
    success_url = '/'
    
    def success(request):
        return render(request, '/')


