from django.contrib import admin
from .models import Restaurant, Review
from django_summernote.admin import SummernoteModelAdmin

# Register Restaurant, review models.
admin.site.register(Restaurant)
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Review model to admin page"""
    summernote_fields = ('body',)
    list_filter = ('created_on', 'approve',)
    list_display = ('name', 'email', 'body', 'created_on',)
