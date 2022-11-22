from django import forms

class CounterTextInput(forms.TextInput):
    template_name = "widgets/counters_text.html"