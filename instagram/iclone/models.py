from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	profile_pic = models.ImageField(upload_to = 'profile', blank = True)
	bio = models.TextField(blank = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.name