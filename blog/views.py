from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request, 'blog/index.html',{"posts" : posts})

def post(request,pk):
    if request.user.is_anonymous:
        messages.info(request, 'You need to SignIn to view full Article.')
        return HttpResponseRedirect(reverse('index'))
    
    posts=Post.objects.get(id=pk)
    return render(request, 'blog/post.html',{"posts" : posts})

def myposts(request):
    if request.user.is_anonymous:
        messages.info(request, "You have not added any post yet")
        return redirect("/blog")
    name=request.user.get_username()
    posts=Post.objects.filter(name=name)
    return render(request, 'blog/myposts.html',{"posts" : posts})

def addpost(request):
    if request.user.is_anonymous:
        messages.info(request, "SignIn to add a Post")
        return render(request, "eauth/signin.html")
    return render(request, "blog/addpost.html")

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

def deletePost(request,pk):
    deletingpost=Post.objects.get(id=pk)
    deletingpost.delete()
    return HttpResponseRedirect(reverse('myposts'))

def games(request):
    return render(request,'blog/games.html')

def mobiles(request):
    query= 'mobile' #request.GET.get('mobile')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'blog/mobiles.html',{"posts" : posts})

def search(request):
    query= request.GET.get('q')
    posts=Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'blog/search.html',{"posts" : posts})
