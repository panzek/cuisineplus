from django.db import models
from cloudinary.models import CloudinaryField


# Create home models.
class Home(models.Model):
    '''Home model
    ---
    Attributes:
        content: Introductory text content to the website
        address: Pyshical address of Cuisine Plus
        hero_image: Hero image of the homepage

    '''
    content = models.TextField(max_length=300, null=True)
    address = models.CharField(max_length=100)
    hero_image = CloudinaryField()
    logo_image = CloudinaryField(null=True)

    def __str__(self):
        return str(self.content)

