from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Restaurant, Review
from .forms import ReviewForm
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
        print(self, request, args, kwargs)
        restaurant = Restaurant.objects.get(pk=kwargs["pk"])

        context = {
            'restaurant': restaurant,
            'review': Review,
            'bookings': Booking,
            "review_form": ReviewForm(),
            "booking_form": BookingForm()
        }

        return render(
            request, 
            'restaurants/restaurant_detail.html',
            context)
    
    """
    Post data to database 
    """

    def post(self, request):
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.review_form = review_form
                review.save()
                return redirect('/')
            else:
                review_form = ReviewForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                "review_form": ReviewForm(),
                "booking_form": BookingForm(),
                "liked": liked,
            },
        )
