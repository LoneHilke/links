from django import forms

from .models import Jango

class JangoForm(forms.ModelForm):

    class Meta:
        model = Jango
        fields = ('titel', 'beskrivelse', 'links')