from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'number_of_guests', 'date', 'time', 'phone', 'additional_info'
            ]
