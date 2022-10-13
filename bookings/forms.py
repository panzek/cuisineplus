from django.forms import ModelForm
from .models import Booking
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'number_of_guests', 'date', 'time', 'phone', 'additional_info'
            ]
        