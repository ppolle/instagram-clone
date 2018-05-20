from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .forms import NewImagePost,CreateComment,UpdateProfile
from .models import Image,Comment,Profile,User,Follow
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
	'''
	Method that fetches all images from all users.
	'''
	images = Image.objects.all()
	title = "Discover"
	
	return render(request,'index.html',{"images":images,"title":title})
def timeline(request):
	'''
	Method that fetches imges from all the users that the current logged in user follows only
	'''
	follows = Follow.objects.filter(user_from = request.user.id)
	images = Image.objects.filter(profile = request.user.following.user_to)
	return render(request, 'accounts/timeline.html',{"images":images,"title":title})


@login_required(login_url='/accounts/login/')
def profile(request,prof_id):
	'''
	Method that fetches a users profile page
	'''
	user=User.objects.get(pk=prof_id)
	images = Image.objects.filter(profile = prof_id)
	title = User.objects.get(pk = prof_id).username
	profile = Profile.objects.filter(user = prof_id)

	if Follow.objects.filter(user_from=request.user,user_to = user).exists():
		is_follow = True
	else:
		is_follow = False

	followers = Follow.objects.filter(user_to = user).count()
	following = Follow.objects.filter(user_from = user).count()
	

	return render(request,'accounts/profile.html',{"images":images,"profile":profile,"title":title,"is_follow":is_follow,"followers":followers,"following":following})
	

@login_required(login_url='/accounts/login/')
def create(request):
	'''
	Method that created an image post
	'''
	current_user = request.user
	profile = Profile.objects.get(user = request.user.id)
	title = "Create New Post"
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.user_profile = profile
			post.save()
			return redirect('profile',current_user.id)
	else:
		
		form = NewImagePost()

	return render(request,'accounts/create_post.html',{"form":form,"title":title})

@login_required(login_url='/accounts/login/')
def updateProfile(request):
	'''
	Method that updates a user's profile.
	'''
	current_user = request.user
	
	title = "Update Profile"
	if request.method == 'POST':
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(request.POST,request.FILES,instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile(request.POST,request.FILES)
		if form.is_valid():
			userProfile = form.save(commit = False)
			userProfile.user = current_user
			userProfile.save()
			return redirect('profile',current_user.id)
	else:
		if Profile.objects.filter(user_id = current_user).exists():
			form = UpdateProfile(instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile()

	return render(request,'accounts/update_profile.html',{"form":form,"title":title})

@login_required(login_url='/accounts/login/')
def single(request,image_id):
	'''
	Method that fetches a single post view.
	'''
	
	image = Image.get_image_by_id(image_id)
	title = image.image_name
	
	if request.method == 'POST':
		form = CreateComment(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.image = image
			comment.profile = request.user
			comment.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		form = CreateComment()

	is_liked = False
	if image.likes.filter(id = request.user.id).exists():
		is_liked = True	
	comments = Comment.objects.filter(image = image_id)
	return render(request,'accounts/single.html',{"image":image,"comments":comments,"form":form,"title":title,"is_liked":is_liked})

@login_required(login_url='/accounts/login/')
def search(request):
	'''
	Method that searches for users based on their profiles
	'''
	if request.GET['search']:
		search_term = request.GET.get("search")
		profiles = Profile.objects.filter(user__username__icontains = search_term)
		message = f"{search_term}"

		return render(request,'accounts/search.html',{"message":message,"profiles":profiles})
	else:
		message = "You haven't searched for any item"
		return render(request,'accounts/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def likePost(request,image_id):
	'''
	Method that likes a post.
	'''
	image = Image.objects.get(pk = image_id)
	
	is_liked = False
	if image.likes.filter(id = request.user.id).exists():
		image.likes.remove(request.user)
		is_liked = False
	else:
		image.likes.add(request.user)
		is_liked = True
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def follow(request,user_to):

   '''
	Method that enables a user to follow another user.
	'''
   user=User.objects.get(id=user_to)
   
   is_follow=False
   if Follow.objects.filter(user_from=request.user,user_to = user).exists():
       Follow.objects.filter(user_from=request.user,user_to = user).delete()
       is_follow=False
   else:
       Follow(user_from=request.user,user_to = user).save()
       is_follow=True
  

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def comment(request):
	'''
	Method that enables a logged in user to comment on an image.
	'''
	comment = request.POST.get('comment')
	comment_made = Comment(comment = comment)
	comment_made.save()
	data = {'success':'You have been succesfully commented on this post'}
	return JsonResponse(data)

def editPost(request,image_id):
	'''
	Method that enables a logged in user to edit posts they created.
	'''
	current_user = request.user
	profile = Profile.objects.get(user = request.user.id)
	image = Image.objects.get(pk = image_id)
	title = "Update Image Post"
	if request.method == 'POST':
		if image:
			form = NewImagePost(request.POST,request.FILES,instance = image)
			if form.is_valid():
				imageUpdate = form.save(commit = False)
				imageUpdate.profile = current_user
				imageUpdate.user_profile = profile
				imageUpdate.save()
				return redirect('profile',current_user.id)
	else:
		form = NewImagePost(instance = image)

	return render(request,'accounts/edit_post.html',{"form":form,"title":title,"image":image})
	