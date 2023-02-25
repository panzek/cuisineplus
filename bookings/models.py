from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from restaurants.models import Restaurant
# from cuisine.models import Cuisine

class Booking(models.Model):
    '''Booking model
    ---
    Attributes:
        user: User that made the booking
        number_of_guests: Number of guests expected
        restaurant: Name of the restaurant being booked
        cuisine: Menu of being booked
        table_number: Table number
        date: Date of the booking
        time: Time of the booking
        additional_info: Any additional information provided

    '''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False, related_name='bookings'
        )
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(null=True)
    number_of_guests = models.IntegerField()
    restaurants = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='bookings'
        )
    cuisine = models.CharField(max_length=100) 
    table_number = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    additional_info = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.last_name)
    