from django import forms
from .models import Person

class PersonFormWithRequest(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []