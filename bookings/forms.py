from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user', 'phone', 'number_of_guests', 'additional_info'
            ]
