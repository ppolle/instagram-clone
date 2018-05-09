from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True)
	bio = models.TextField(blank = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user

class Image(models.Model):
	image = models.ImageField(upload_to = 'images/')
	image_name = models.CharField(max_length = 60)
	image_caption = models.CharField(max_length = 60)
	proile = models.ForeignKey(User)

	def __str__(self):
		return self.image_name

class Comment(models.Model):
	comment = models.TextField()
	image = models.ForeignKey(Image)
	profile = models.ForeignKey(User)

	def __str__(self):
		return self.profile