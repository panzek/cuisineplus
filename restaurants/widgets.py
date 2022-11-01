from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'restaurants/datepicker.html'