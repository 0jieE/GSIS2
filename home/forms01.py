from typing_extensions import Required
from django import forms
from django.forms import widgets

from .models import Enrollment, EnrollmentDetail, Class_Schedule, SubjectTaken, Subject

class EnrollForm(forms.Form):
    enrollment = forms.ModelChoiceField(queryset=Enrollment.objects.all(), label="Enrollment")
    year_level = forms.CharField(max_length=10, label="Year level")
    schedules = forms.ModelMultipleChoiceField(queryset=Class_Schedule.objects.none(),
                widget=forms.CheckboxSelectMultiple, label="Schedules", required=False)

    
    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semester'].widget.attrs['onChange'] = 'this.form.submit();'
        self.fields['schedules'].queryset = Class_Schedule.objects.none()

        if 'semester' in self.data:
            semester_id = int(self.data.get('semester'))
            year_level = self.data.get('year_level')
            self.fields['schedules'].queryset = Class_Schedule.objects.filter(
                semester_id=semester_id,
                year_level=year_level
            )