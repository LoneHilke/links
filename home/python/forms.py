from django import forms

from .models import Python

class PythonForm(forms.ModelForm):

    class Meta:
        model = Python
        fields = ('title', 'beskrivelse', 'links')