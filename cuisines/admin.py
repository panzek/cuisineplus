from django.contrib import admin
from .models import Menu, Review
from django_summernote.admin import SummernoteModelAdmin

# Register menu, review models.
@admin.register(Menu)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Menu model to admin page"""
    pass

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """ Add Review model to admin page"""
    summernote_fields = ('body',)
