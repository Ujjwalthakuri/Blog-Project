from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *
# Create your views here.
 
def home(request):
    return render (request, 'base_cont/home.html')

 
 

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'email':'', 'password1':'', 'password2':''}
        form = CustomUserCreationForm(initial = initial_data)
    return render(request, 'base_cont/signup.html', {'form': form})


    
    
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # important: pass request as first arg
        if form.is_valid():
            user = form.get_user()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            login(request, user)
            return redirect('index')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm( initial = initial_data)
    return render(request, 'base_cont/signin.html', {'form': form})


def index(request):
    post = postModel.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('index')
    else:
        form = PostForm()

    context = {
        'post': post,
        'forms': form
    }
    return render(request, 'main_cont/index.html', context)

def profile(request):
    
    # Get posts by the current user
    user_posts = postModel.objects.filter(author=request.user)

    # Get the profile for the current user
    try:
        user_profile = profileModel.objects.get(author=request.user)
    except profileModel.DoesNotExist:
        user_profile = None  # or handle redirect to profile creation

    context = {
        'post': user_posts,
        'profile': user_profile
    }
    return render(request, 'main_cont/profile.html', context)


def signout(request):
    logout(request)
    return redirect ('home')

def post(request):
    return HttpResponse



 