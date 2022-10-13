from django.shortcuts import render
from django.views import generic
from .models import Restaurant

class RestaurantList(generic.ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'

    context = {
        'restaurants': Restaurant.objects.all()
    }