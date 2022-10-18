from django.shortcuts import render, redirect
from django.views import generic
from .models import Restaurant

class RestaurantList(generic.ListView):
    model = Restaurant
    queryset: Restaurant.objects.all().order_by('name')
    template_name = 'restaurants/restaurant_list.html'
    pagination = 8

    # context = {
    #     'restaurants': Restaurant.objects.all()
    # }

    
    # """
    # Get data from forms.py and render in restaurant_form
    # """

    # def get(self, request): 
    #     return render(
    #         request, "restaurants/restaurant_list.html",
    #         {
    #             "restaurant_form": RestaurantForm()
    #         }
           
    #     )

    # """
    # Post data to database 
    # """

    # def post(self, request):
    #     if request.method == 'POST':
    #         restaurant_form = RestaurantForm(request.POST)
    #         if restaurant_form.is_valid():
    #             restaurant = restaurant_form.save(commit=False)
    #             restaurant.restaurant_form = restaurant_form
    #             restaurant.save()
    #             return redirect('/')
    #         else:
    #             restaurant_form = RestaurantForm()

    #     return render(
    #         request, 
    #         "restaurants/restaurant_list.html", 
    #         {
    #             "restaurant_form": RestaurantForm()
    #         }
    #     )


