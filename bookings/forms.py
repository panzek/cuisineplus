from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'firstname', 'lastname', 'phone', 'email', 'number_of_guests', 'additional_info'
            ]