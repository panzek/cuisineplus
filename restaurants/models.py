from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phone_field import PhoneField
from django import forms
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
    reserve = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    rating = models.IntegerField(blank=True)
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
    cuisine = models.PositiveSmallIntegerField(choices=CUISINE_TYPES, null=True)
    
    featured_image = CloudinaryField()

    def __str__(self):
        return str(self.name)

    def number_of_likes(self):
        return self.likes.count()


class Menu(models.Model):
    '''Menu model
    ---
    Attributes:
        name: Name of the cuisine
        menu: Details of the food to be served
        price: Price of the cuisine
        cuisine: Type of cuisine such as Chinese, African, Irish, continental
        status: States whether the cuisine is ready or not
        cuisine_image: Photo image of the cuisine
        created_on: Date and time created
        updated_on: Date and time updated

    '''

    STATUS = ((0, "Not Ready"), (1, "Ready"))

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='restaurant_menu'
    )
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
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
    approve = models.BooleanField(default=False)

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

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.name)
