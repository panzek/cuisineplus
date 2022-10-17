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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False, related_name='restaurants'
        )
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


class Cuisine(models.Model):
    '''Cuisine model
    ---
    Attributes:
        name: Name of the cuisine 
        menu: Details of the food to be served
        price: Price of the cuisine
        cuisine: Type of cuisine such as Chinese, African, Irish, intercontinental
        status: States whether the cuisine is ready or not
        likes: Customer ratings
        cuisine_image: Photo image of the cuisine
        created_on: Date and time created
        updated_on: Date and time updated

    '''

    STATUS = ((0, "Not Ready"), (1, "Ready")) 

    restaurants = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_cuisines')
    name = models.CharField(max_length=100, null=True)
    menu = models.CharField(max_length=100)
    price = models.FloatField()
    cuisine = models.PositiveSmallIntegerField(choices=(
        (1, 'African'),
        (2, 'Chinese'),
        (3, 'Asian'),
        (1, 'Irish'),
        (1, 'Continental'),
    ), null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='cuisine_likes', blank=True)
    cuisine_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return str(self.name)

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):
    '''Cuisine model
    ---
    Attributes:
        name: Name of the cuisine 
        body: Customer comments
        created_on: Date and time created
        approved: Approval status

    '''

    name = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=350, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"

