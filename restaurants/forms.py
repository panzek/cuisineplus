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
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write a Review'}))


    class Meta:
        model = Review
        fields = [
            'name',
            'body', 
        ]


class ReservationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    number_of_guests = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Time'}))
    additional_info = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Comments'}))

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
