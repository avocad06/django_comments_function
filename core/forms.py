from django import forms
from .models import University, Student
from .widgets import CounterTextInput

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }
    