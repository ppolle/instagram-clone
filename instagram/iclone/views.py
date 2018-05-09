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
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.save()
			HttpResponseRedirect('profile')
	else:
		
		form = NewImagePost()
	images = Image.objects.filter(profile = current_user)
	return render(request,'accounts/profile.html',{"form":form,"images":images})


