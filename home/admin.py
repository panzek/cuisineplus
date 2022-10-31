from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Home)
class HomeAdmin(SummernoteModelAdmin):
    """ Add Home model to admin page"""
    summernote_fields = ('content', 'address',)
