from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# from restaurant.models import Restaurant
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
        User, on_delete=models.CASCADE, related_name='bookings'
        )
    phone = PhoneField(blank=True, help_text='Contact phone number')
    number_of_guests = models.IntegerField()
    # restaurant = models.ForeignKey(
    #     Restaurant, on_delete=models.CASCADE, related_name='bookings'
    #     )
    restaurant = models.CharField(max_length=100)
    # cuisine = models.ForeignKey(
    #     Cuisine, on_delete=models.CASCADE, related_name='bookings'
    #     )
    cuisine = models.CharField(max_length=100)
    table_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    additional_info = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.user)
    