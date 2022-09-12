from django import forms
from .models import Imageadd

class ImageAddForm(forms.ModelForm):
    class Meta:
        model = Imageadd
        fields = ('name', 'image')
        