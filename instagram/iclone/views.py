from django.shortcuts import render,redirect
from .forms import NewImagePost
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	
	return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewImagePost(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit =  False)
			post.profile = current_user
			post.save()
	else:
		form = NewImagePost()
	return render(request,'accounts/profile.html',{"form":form})


