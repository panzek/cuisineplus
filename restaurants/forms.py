from django.forms import ModelForm
from django import forms
from .models import Restaurant, Review, Reservation, Menu
from datetime import datetime
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.forms.widgets import DateInput


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'featured_image',
        ]


class MenuForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write a menu List'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the menu'}))
    class Meta:
        model = Menu
        fields = [
            'name',
            'description',
            'body',
            'price',
        ]


class ReviewForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write a Review'}))

    class Meta:
        model = Review
        fields = [
            'body',
        ]


class ReservationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    number_of_guests = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}))
    date = forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d"), 
        widget=forms.widgets.DateInput(attrs={
            'type': 'date', 
            'class': 'form-control', 
            'placeholder': 'Enter Date'
            }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time', 
        'class': 'form-control', 
        'placeholder': 'Enter Time'
        }))
        
    additional_info = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'rows': 5, 
        'placeholder': 'Your Comments'
        }))

    
    # class DateInput(forms.DateInput):
    #     input_type = 'date'
    class Meta:
        model = Reservation
        fields = [
            'name',
            'number_of_guests',
            'date',
  
            'time',
            # 'phone',
            'additional_info'
        ]

        # widgets = {
        #     'date': DateInput(),
        # }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['date'].widgets = forms.widgets.DateInput(
        #         attrs={'type': 'date'})
        #     self.fields['start_time'].widget = forms.widgets.TimeInput(
        #         attrs={'type': 'time'})

        # widgets = {
        #     "date": DatePickerInput(options={
        #         "format": "MM/DD/YYYY",
        #         "showClose": True,
        #         "showClear": True,
        #         "showTodayButton": True,
        #         "defaultDate": True,
        #         }),
        #     "time": TimePickerInput(),
        # }


    
        # widgets = {
        # 'date': forms.DateInput(
        #     attrs={'class': 'form-control',
        #     'placeholder': 'Select a date',
        #     'type': 'date'
        #     }),
        # }
    
    # class DateInput(forms.DateInput):
    #     input_type = 'date'

    
    # }

    # def clean(self):
    #     cleaned_data = super(ReservationForm, self).clean()
    #     my_date = self.cleaned_data.get('date')
    #     my_time = self.cleaned_data.get('time')

    #     if my_date and my_time:
    #         my_date_time = (my_date + ' ' + my_time + ':00')
    #         my_date_time = datetime.strptime(my_date_time, '%m/%d/%Y %H:%M:%S')
    #         if datetime.now() <= my_date_time:
    #             msg = u"Wrong Date time !"
    #             self.add_error('my_date', msg)
    #             self.add_error('my_time', msg)
    #     return cleaned_data
        # if date < datetime.today().date():
        #     raise ValidationError("Invalid date - Booking cannot be in the past")
        # if number_of_guests < 1 or number_of_guests > 6:
            # raise ValidationError("Enter a number between 1 and 6")
        # return number_of_guests