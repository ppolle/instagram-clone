from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True)
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user

class Image(models.Model):
	
	image_name = models.CharField(max_length = 60)
	image_caption = models.CharField(max_length = 60)
	# created_at = models.DateTimeField(auto_now_add = True)
	profile = models.ForeignKey(User)
	image = models.ImageField(upload_to = 'images/')

	def __str__(self):
		return self.image_name

class Comment(models.Model):
	comment = models.CharField(max_length = 1000)
	# created_at = models.DateTimeField(auto_now_add = True)
	image = models.ForeignKey(Image)
	profile = models.ForeignKey(User)

	def __str__(self):
		return self.profile

class Follow(models.Model):
      following = models.ForeignKey(User, related_name="who_follows")
      follower = models.ForeignKey(User, related_name="who_is_followed")

