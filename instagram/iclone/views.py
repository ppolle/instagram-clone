from django.shortcuts import render,redirect
from .forms import NewImagePost
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	form = NewImagePost()
	return render(request,'index.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
	return render(request,'accounts/profile.html')
