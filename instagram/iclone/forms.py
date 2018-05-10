from django import forms
from .models import Image,Profile

class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']
       
class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']