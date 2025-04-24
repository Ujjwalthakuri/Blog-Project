from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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

@login_required
def index(request):
    categories = CategoryModel.objects.all()
    posts = postModel.objects.all()

    # Handle filtering
    title = request.GET.get('title')
    category = request.GET.get('category')
    author = request.GET.get('author')

    if title:
        posts = posts.filter(title__icontains=title)
    if category:
        posts = posts.filter(category__id=category)
    if author:
        posts = posts.filter(author__username__icontains=author)

    # Handle new post creation
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
        'post': posts,
        'forms': form,
        'categories': categories,
    }
    return render(request, 'main_cont/index.html', context)

@login_required
def profile(request):
    # Ensure the user has a profilemodel
    profile, created = profileModel.objects.get_or_create(author=request.user)

    if request.method == 'POST':
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    # Get posts by the current user
    user_posts = postModel.objects.filter(author=request.user)

    context = {
        'post': user_posts,
        'profile': profile,
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'main_cont/profile.html', context)


@login_required
def post_detail(request, pk):
    post = postModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance= c_form.save(commit=False)
            instance.user = request.user
            instance.post = post 
            instance.save()
            return redirect ('postdetail', pk=post.id)
    else:
        c_form = CommentForm()
    context={
        'post':post,
        'c_form': c_form
    }
    return render(request, 'main_cont/postdetail.html', context)


@login_required
def post_edit(request, pk):
    post = postModel.objects.get(id=pk)
    if request.method =="POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("postdetail", pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post' : post,
        "form": form
    }
    return render(request, 'main_cont/postedit.html', context)

@login_required
def post_del(request, pk):
    post = postModel.objects.get(id=pk)
    if request.method =="POST":
        post.delete()
        return redirect("profile")
    context={
        'post':post,
    }
    return render(request, 'main_cont/postdel.html', context)



def signout(request):
    logout(request)
    return redirect ('home')

# def post(request):
#     return HttpResponse
@login_required
def search_posts(request):
    form = PostFilterForm(request.GET)
    posts = postModel.objects.none()  # empty initially
    searched = False

    if request.GET:
        searched = True
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')
            author = form.cleaned_data.get('author')
            date = form.cleaned_data.get('start_date')

            posts = postModel.objects.all()
            if title:
                posts = posts.filter(title__icontains=title)
            if category:
                posts = posts.filter(category=category)
            if author:
                posts = posts.filter(author__username__icontains=author)
            if date:
                posts = posts.filter(published_date__gte=date)

    return render(request, 'main_cont/search_results.html', {
        'form': form,
        'posts': posts,
        'searched': searched
    })
