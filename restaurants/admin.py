from django.contrib import admin
from .models import Restaurant, Review, Reservation, Menu
from django_summernote.admin import SummernoteModelAdmin

# Register Restaurant, Menu, Reservation, and review models.


@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    """ Add Restaurant model to admin page"""
    list_filter = ('name', 'address',)
    list_display = ('name', 'address',)
    search_fields = ('name', 'Restaurant',)


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    """ Add Menu model to admin page"""
    list_filter = ('name',)
    list_display = ('name', 'price', 'description', 'body', 'restaurants',)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Review model to admin page"""
    summernote_fields = ('body',)
    list_filter = ('created_on', 'approved',)
    list_display = ('name', 'body', 'created_on', 'approved', 'restaurants',)
    search_fields = ('name', 'email', 'body',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    """ Add Reservation model to admin page"""
    summernote_fields = ('additional_info',)
    list_filter = ('name', 'restaurants',)
    list_display = (
        'name',
        'number_of_guests',
        'date',
        'time',
        'phone',
        'additional_info',
        'created_on',
        'updated_on',
        'restaurants',
    )
    