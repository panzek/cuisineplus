from django.forms import ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 
            'address', 
            'time', 
            'cuisines', 
            'reserve', 
            'rating', 
            'price', 
            'review'
        ]
        

