from django import forms

from .models import Sidebar

class SidebarForm(forms.ModelForm):

    class Meta:
        model = Sidebar
        fields = ('title', 'text', 'link')