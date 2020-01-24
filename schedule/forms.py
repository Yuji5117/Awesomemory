from django import forms

from .models import Schedule

class DateInput(forms.DateInput):
    input_type = 'date'


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = (
            'date',
            'title',
            'content'
            )
        # HTML input_type:date
        widgets = {'date': DateInput()}
    
    
