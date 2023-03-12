from django.shortcuts import render, redirect
from post.models import Post
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request, 'index.html',{"posts" : posts})

def post(request,pk):
    if request.user.is_anonymous:
        messages.info(request, 'You need to SignIn to view full Article.')
        return HttpResponseRedirect(reverse('index'))
    
    posts=Post.objects.get(id=pk)
    return render(request, 'post.html',{"posts" : posts})

def myposts(request):
    name=request.user.get_username()
    posts=Post.objects.filter(name=name)
    return render(request, 'myposts.html',{"posts" : posts})

def games(request):
    return render(request,'games.html')

def addpost(request):
    if request.user.is_anonymous:
        return render(request, "signin.html")
    return render(request, "addpost.html")

def deletePost(request,pk):
    deletingpost=Post.objects.get(id=pk)
    deletingpost.delete()
    return HttpResponseRedirect(reverse('myposts'))
    
    
    
def upload(request):
    if request.method=="POST":
        name=request.user.get_username()
        title=request.POST.get('title')
        body=request.POST.get('body')
        yourblog=Post(name=name,title=title,body=body,)
        yourblog.save()
        messages.success(request, 'Your blog has been posted.Keep posting. Thank you!!')#show message in admin panel and webpage
        # messages.info(request, 'Thanks for adding new blog. Keep Posting.')# show message in webpage
    return HttpResponseRedirect(reverse('myposts'))
      

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not a valid User')
            return redirect('/signin')
    else:
        return render(request, "signin.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request,'Password not same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/signin')

def mobiles(request):
    query= 'mobile' #request.GET.get('mobile')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'mobiles.html',{"posts" : posts})

def games(request):
    query= 'games' #request.GET.get('mobile')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'games.html',{"posts" : posts})

def gadgets(request):
    query= 'gadgets' #request.GET.get('mobile')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'gadgets.html',{"posts" : posts})

def search(request):
    query= request.GET.get('q')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'search.html',{"posts" : posts})