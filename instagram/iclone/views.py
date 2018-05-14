from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewImagePost,CreateComment,UpdateProfile
from .models import Image,Comment,Profile,User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	images = Image.objects.all()
	return render(request,'index.html',{"images":images})


@login_required(login_url='/accounts/login/')
def profile(request,prof_id):
	current_user = request.user
	images = Image.objects.filter(profile = prof_id)
	title = current_user
	profile = Profile.objects.filter(user = prof_id)
	return render(request,'accounts/profile.html',{"images":images,"profile":profile,"title":title})
	

@login_required(login_url='/accounts/login/')
def create(request):
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
	current_user = request.user
	
	title = "Update Profile"
	if request.method == 'POST':
		if Profile.objects.filter(user_id = current_user):
			form = UpdateProfile(request.POST,request.FILES,instance = Profile.objects.get(user_id = current_user))
		else:
			form = UpdateProfile(request.POST,request.FILES)
		if form.is_valid():
			userProfile = form.save(commit = False)
			userProfile.user = current_user
			userProfile.save()
			return redirect('profile',current_user.id)
	else:
		form = UpdateProfile()

	return render(request,'accounts/update_profile.html',{"form":form})

def single(request,image_id):
	
	image = Image.get_image_by_id(image_id)
	title = image.image_name
	if request.method == 'POST':
		form = CreateComment(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.image = image
			comment.profile = request.user
			comment.save()
			HttpResponseRedirect('single')
	else:
		form = CreateComment()


	comments = Comment.objects.filter(image = image_id)
	return render(request,'accounts/single.html',{"image":image,"comments":comments,"form":form,"title":title})

def search(request):
	if request.GET['search']:
		search_term = request.GET.get("search")
		profiles = User.objects.filter(username__icontains = search_term)
		message = f"{search_term}"

		return render(request,'accounts/search.html',{"message":message,"profiles":profiles})
	else:
		message = "You haven't searched for any item"
		return render(request,'accounts/search.html',{"message":message})
