from django.forms import ModelForm
from django import forms
from .models import Restaurant, Review, Reservation, Menu
from datetime import datetime


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'featured_image',
        ]


class MenuForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write a menu List'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the menu'}))

    class Meta:
        model = Menu
        fields = [
            'name',
            'description',
            'body',
            'price',
        ]


class ReviewForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write a Review'}))

    class Meta:
        model = Review
        fields = [
            'body',
        ]


class ReservationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    number_of_guests = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}))
    date = forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d"), 
        widget=forms.widgets.DateInput(attrs={
            'type': 'date', 
            'class': 'form-control', 
            'placeholder': 'Enter Date'
            }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time', 
        'class': 'form-control', 
        'placeholder': 'Enter Time'
        }))
        
    additional_info = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'rows': 5, 
        'placeholder': 'Your Comments'
        }))

    class Meta:
        model = Reservation
        fields = [
            'name',
            'number_of_guests',
            'date',
            'time',
            'additional_info'
        ]

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['number_of_guests'].widget.attrs['min'] = 1
        