from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Restaurant(models.Model):
    '''Restaurant model
    ---
    Attributes:
        name: Name of the restaurant 
        reserve: Reservations made by guests
        avg_rating: Average number of ratings by customers
        location: Address of restaurant
        cuisines: Menu on offer
        featured_image: Photo image of the restaurant
        review: Customers' review of the restaurant

    '''

    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    time = models.TimeField()
    cuisines = models.CharField(max_length=100, null=True)
    reserve = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(blank=True)
    price = models.FloatField()
    review = models.TextField(max_length=500, null=True)
    featured_image = CloudinaryField('image')

    def __str__(self):
        return str(self.name)
    