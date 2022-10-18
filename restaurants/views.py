from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Restaurant

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
            'restaurant': restaurant
        }

        return render(request, 'restaurants/restaurant_detail.html', context)
