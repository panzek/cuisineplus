from django.forms import ModelForm
from .models import Restaurant, Review

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
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'name', 
            'email', 
            'body', 
            'created_on',
        ]
        
