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
            "reviewed": False,
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

    # def post(self, request):
    #     if request.method == 'POST':
    #         review_form = ReviewForm(request.POST)
    #         if review_form.is_valid():
    #             review = review_form.save(commit=False)
    #             review.review_form = review_form
    #             review.save()
    #             return redirect('/')
    #         else:
    #             review_form = ReviewForm()

    #     return render(
    #         request, 
    #         "restaurants/restaurant_detail.html", 
    #         {
    #             "review_form": ReviewForm(),
    #             "booking_form": BookingForm(),
    #             "liked": liked,
    #         },
    #     )
    
    def post(self, request, pk, *args, **kwargs):
        review = get_object_or_404(Review, pk=1)
        # review.Review.filter(approved=True).order_by('created_on')
        
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.user = request.user.username 
            review = review_form.save(commit=False)
            review.review = review
            review.save()
            return redirect('/')
        else:
            review_form = ReviewForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                'restaurant': Restaurant,
                'review': Review,
                "reviewed": True,
                'bookings': Booking,
                "review_form": ReviewForm(),
                "booking_form": BookingForm()
            },
        )

