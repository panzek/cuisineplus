from cloudinary.models import CloudinaryField
from django import forms
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
from phone_field import PhoneField

from .widgets import FengyuanChenDatePickerInput


class Restaurant(models.Model):
    '''Restaurant model
    ---
    Attributes:
        name: Name of the restaurant
        reserve: Reservations made by guests
        avg_rating: Average number of ratings by customers
        location: Address of restaurant
        featured_image: Photo image of the restaurant

    '''

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='restaurants'
        )
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=1500, null=True)
    likes = models.ManyToManyField(
        User, related_name='restaurant_likes', blank=True
    )
    CUISINE_TYPES = (
        (1, 'African'),
        (2, 'Chinese'),
        (3, 'Asian'),
        (4, 'Irish'),
        (5, 'Continental')
    )
    cuisine = MultiSelectField(choices=CUISINE_TYPES, max_choices=5, max_length=5, null=True)

    OPERATION_HOURS = (
        (1, '11:00am - 08:00pm'),
        (2, '12:00am - 08:00pm'),
        (3, '12:00am - 10:00pm'),
        (4, '01:00pm - 09:00pm'),
        (5, '03:00pm - 09:00pm'),
        (6, '03:00pm - 10:00pm'),
    )
    time = models.PositiveSmallIntegerField(choices=OPERATION_HOURS, null=True)
    
    featured_image = CloudinaryField()

    def __str__(self):
        return str(self.name)

    def number_of_likes(self):
        return self.likes.count()


class Menu(models.Model):
    '''Menu model
    ---
    Attributes:
        name: Name of the menu
        menu: Details of the food to be served
        price: Price of the menu
        menu_image: Photo image of the menu
        created_on: Date and time created
        updated_on: Date and time updated

    '''

    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menus'
    )
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=3500, null=True)
    body = models.TextField(max_length=2500, null=True)
    price = models.FloatField()
    menu_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    '''Review model
    ---
    Attributes:
        name: Name of the reviewer
        body: Customer comments
        created_on: Date and time created
        approved: Approval status

    '''

    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, related_name='reviews'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(max_length=250, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"


class Reservation(models.Model):
    '''Reservation model
    ---
    Attributes:
        name: Name of the person that made the booking
        number_of_guests: Number of guests expected
        restaurant: Name of the restaurant being booked
        table_number: Table number
        date: Date of the booking
        time: Time of the booking
        additional_info: Any additional information provided
    '''
    date = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=FengyuanChenDatePickerInput()
        )

    restaurants = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        null=True,
        related_name='reservations'
    )
    name = models.CharField(max_length=100)
    phone = PhoneField(blank=True)
    number_of_guests = models.IntegerField()
    table_number = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    additional_info = models.TextField(max_length=150, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.name)
