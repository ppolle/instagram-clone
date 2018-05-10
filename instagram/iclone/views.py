from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewImagePost
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	images = Image.objects.all()
	return render(request,'index.html',{"images":images})


@login_required(login_url='/accounts/login/')
def profile(request):
	current_user = request.user
	images = Image.objects.filter(profile = current_user)
	return render(request,'accounts/profile.html',{"images":images})

@login_required(login_url='/accounts/login/')
def create(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.save()
			HttpResponseRedirect('profile')
	else:
		
		form = NewImagePost()

	return render(request,'accounts/create_post.html',{"form":form})

@login_required(login_url='/accounts/login/')
def updateProfile(request):
	current_user = request.user
	if request.method == 'POST':
		form = UpdateProfile(request.POST,request.FILES)
		if form.is_valid():
			profile = form.save(commit = False)
			profile.user = current_user
			profile.save()
			HttpResponseRedirect('profile')
		else:
			form = UpdateProfile()

	return render(request,'accounts/update_profile.html',{"form":form})

def single(request,image_id):
	image = Image.objects.get(id = image_id)
	return render(request,'accounts/single.html',{"image":image})