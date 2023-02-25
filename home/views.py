from django.shortcuts import render
from restaurants.models import Restaurant


def Home(request):
    """
    View to display the site's home page
    """

    restaurants = Restaurant.objects.all()

    context = {
        'restaurant_list': restaurants
    }

    return render(request, 'home/index.html', context)
