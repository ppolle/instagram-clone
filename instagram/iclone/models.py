from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True,default = 'Awesome Bio Will Appear Here')
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True,default = 'profile/default.png')
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user

class Image(models.Model):
	
	image_name = models.CharField(max_length = 60)
	image_caption = models.CharField(max_length = 60)
	created_at = models.DateTimeField(auto_now_add = True)
	profile = models.ForeignKey(User)
	user_profile = models.ForeignKey(Profile)
	likes = models.ManyToManyField(User,related_name = 'likes', blank = True)
	image = models.ImageField(upload_to = 'images/')

	@classmethod
	def save_image(self):
		self.save()

	@classmethod
	def delete_image(self):
		self.delete()

	@classmethod
	def update_caption(cls,id,caption):
		updated_caption = cls.objects.filter(pk = id).update(image_caption = caption)
		return updated_location	

	@classmethod
	def get_image_by_id(cls,image_id):
		image = cls.objects.get(id = image_id)
		return image
	def total_likes(self):
		self.likes.count()

	def __str__(self):
		return self.image_name

class Comment(models.Model):
	comment = models.CharField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	image = models.ForeignKey(Image)
	profile = models.ForeignKey(User)

	def __str__(self):
		return self.profile

class Follow(models.Model):
    user_from = models.ForeignKey(User,related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


# Add following field to User dynamically
User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Follow,
                                         related_name='followers',
                                         symmetrical=False))
