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
        featured_image: Photo image of the restaurant

    '''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False, related_name='restaurants'
        )
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    reserve = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(blank=True)
    featured_image = CloudinaryField()

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
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    body = models.TextField(max_length=350, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"


