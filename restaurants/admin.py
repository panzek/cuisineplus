from django.contrib import admin
from .models import Restaurant, Review, Menu
from django_summernote.admin import SummernoteModelAdmin

# Register Restaurant, review models.
# admin.site.register(Restaurant)

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    """ Add Restaurant model to admin page"""
    list_filter = ('name', 'address',)
    list_display = ('name', 'address', 'rating',)
    search_fields = ('name', 'Restaurant',)

@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    """ Add Menu model to admin page"""
    list_filter = ('status', 'created_on',)
    list_display = ('name', 'price', 'status', 'created_on',)
    search_fields = ('date', 'time', 'number_of_guests', 'cuisine',)
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Review model to admin page"""
    summernote_fields = ('body',)
    list_filter = ('created_on', 'approve',)
    list_display = ('name', 'email', 'body', 'created_on',)
