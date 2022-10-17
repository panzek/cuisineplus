from django.contrib import admin
from .models import Menu, Review
from django_summernote.admin import SummernoteModelAdmin

# Register menu, review models.
@admin.register(Menu)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Menu model to admin page"""
    list_filter = ('status', 'created_on',)
    list_display = ('name', 'price', 'status', 'created_on',)
    search_fields = ('date', 'time', 'number_of_guests', 'cuisine',)

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Review model to admin page"""
    summernote_fields = ('body',)
    list_filter = ('created_on', 'approved',)
    list_display = ('title', 'menu', 'created_on',)
