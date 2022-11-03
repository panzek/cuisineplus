from django.forms import ModelForm
from django import forms
from .models import Restaurant, Review, Reservation

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
            'body', 
        ]

class ReservationForm(ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    additional_info = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Reservation
        fields = [
            'name', 
            'number_of_guests', 
            'date', 
            'time', 
            'phone', 
            'additional_info'
        ]    
