from django import forms
from .models import Image,Comment,Profile

class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','user_profile','likes']
       
class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio','profile_pic']
		exclude = ['user']

class CreateComment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
		exclude = ['image','profile']