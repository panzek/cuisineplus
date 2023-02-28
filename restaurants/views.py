from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from restaurants.models import Restaurant, Review, Reservation, Menu
from .forms import ReviewForm, ReservationForm, MenuForm
from bookings.forms import BookingForm
from bookings.models import Booking


class RestaurantList(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.all()
    template_name = 'restaurants/restaurant_list.html'
    pagination = 4


class RestaurantDetail(generic.DetailView):

    model = Restaurant

    def get(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.get(pk=kwargs["pk"])
        reviews = Review.objects.filter(restaurants=restaurant, approved=True)
        reservations = Reservation.objects.filter(restaurants=restaurant)
        menus = Menu.objects.filter(restaurants=restaurant)
        liked = False
        if restaurant.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            'restaurant': restaurant,
            'reviews': reviews,
            'reviewed': False,
            'reservations': reservations,
            'menus': menus,
            'bookings': Booking,
            'liked': liked,
            'review_form': ReviewForm(),
            'menu_form': MenuForm(),
            'reservation_form': ReservationForm(),
            'booking_form': BookingForm(),
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
        reviews = Review.objects.filter(restaurants=restaurant, approved=True)
        reservation_form = ReservationForm(data=request.POST)
        liked = False
        if restaurant.likes.filter(id=self.request.user.id).exists():
            liked = True

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
                request, "Your review successfully submitted, but awaiting approval"
                )
            return HttpResponseRedirect(reverse('restaurant_detail', args=[pk]))
        else:
            review_form = ReviewForm()

        menu_form = MenuForm(data=request.POST)
        if menu_form.is_valid():
            menu.email = request.user.email
            menu.name = request.user.username
            menu = menu_form.save(commit=False)
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
                'reviews': reviews,
                'reviewed': True,
                'liked': liked,
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


class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'restaurants/delete_reservation.html'
    success_url = reverse_lazy('reservation')


class RestaurantLike(View):
    def post(self, request, pk, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        if restaurant.likes.filter(id=self.request.user.id).exists():
            restaurant.likes.remove(request.user)
        else:
            restaurant.likes.add(request.user)
        return HttpResponseRedirect(reverse('restaurant_detail', args=[pk]))
