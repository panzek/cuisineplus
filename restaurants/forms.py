from django.forms import ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 
            'address', 
            'reserve', 
            'rating',
            'featured_image', 
        ]
        

