from django.forms import ModelForm
from booking.models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'firstname', 'lastname', 'email', 'phone_number', 'notes',
            ]