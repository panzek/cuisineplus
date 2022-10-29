from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

# Register models 
# admin.site.register(Booking)
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """ Add Booking model to admin page"""
    summernote_fields = ('additional_info',)
    list_filter = ('number_of_guests', 'restaurants',)
    list_display = ('number_of_guests', 'date', 'time', 'phone', 'additional_info', 'restaurants',)
