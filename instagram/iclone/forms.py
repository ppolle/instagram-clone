from django import forms
from .models import Image

class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']
       