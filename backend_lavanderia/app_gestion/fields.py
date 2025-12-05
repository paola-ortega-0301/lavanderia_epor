from django import forms

class CustomDateField(forms.DateField):
    def __init__(self, **kwargs):
        kwargs.setdefault('input_formats', ('%Y-%m-%d',)) # Define el formato de fecha
        super().__init__(**kwargs)
