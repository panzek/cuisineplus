from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.views.generic.base import TemplateView
from restaurants.models import Restaurant


# class HomePageView(TemplateView):
#     """
#     View to display the site's home page
#     """
#     template_name = 'home/index.html'

def Home(request):
    """
    View to display the site's home page
    """

    restaurants = Restaurant.objects.all()

    context = {
 
        'restaurant_list': restaurants
    }

    return render(request, 'home/index.html', context)

