from django.views.generic.base import TemplateView
from restaurants.models import Restaurant, Review, Reservation

class HomePageView(TemplateView):
    """
    View to display the site's home page
    """
    template_name = 'home/index.html'