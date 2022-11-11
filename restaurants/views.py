from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from restaurants.models import Restaurant, Review, Reservation, Menu
from .forms import ReviewForm, ReservationForm, MenuForm
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
        menus = Menu.objects.filter(restaurants=restaurant)

        context = {
            'restaurant': restaurant,
            'reviews': reviews,
            'reviewed': True,
            'reservations': reservations,
            'menus': menus,
            "reviewed": False,
            'bookings': Booking,
            "review_form": ReviewForm(),
            "menu_form": MenuForm(),
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
    # --- Review and Reservation view ---
    def post(self, request, pk, *args, **kwargs):
        restaurant = Restaurant.objects.get(id=request.POST.get("restaurant"))
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.email = request.user.email
            reservation.name = request.user.username
            reservation.restaurants = restaurant
            reservation_form.save()
            messages.success(
                request, "Your reservation successfully submitted"
                )
            return HttpResponseRedirect(request.path_info)
        else:
            reservation_form = ReservationForm()

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.restaurants = restaurant
            review.save()
            messages.success(
                request, "Your review successfully submitted"
                )
            return HttpResponseRedirect(request.path_info)
        else:
            review_form = ReviewForm()
        
        if menu_form.is_valid():
            menu = menu_form.save(commit=False)
            menu.email = request.user.email
            menu.name = request.user.username
            menu.restaurants = restaurant
            menu_form.save()
            return redirect('/')
        else:
            menu_form = MenuForm()

        return render(
            request, 
            "restaurants/restaurant_detail.html", 
            {
                'restaurant': Restaurant,
                'reviewed': True,
                "reservation_form": ReservationForm(),
            },
        )


class MenuList(generic.ListView):
    model = Menu
    queryset: Restaurant.objects.all()
    template_name = 'restaurants/menu_list.html'
    pagination = 8


class ReservationList(generic.ListView):
    model = Reservation
    queryset: Restaurant.objects.all()
    template_name = 'restaurants/reservation_list.html'
    pagination = 8

#  --- Reservation Update ---
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurants/edit_reservation.html'
    success_url = '/'
    
    def success(request):
        return render(request, '/')


class ReservationDeleteView(PermissionRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'restaurants/delete_reservation.html'
    success_url = reverse_lazy('reservation')
    permission_required = ('reservation.delete_reservation')

    def has_permission(self):
        has_perms = super().has_permission()
        self.object = self.get_object()
        author = self.object.author == self.request.user  
        return author



