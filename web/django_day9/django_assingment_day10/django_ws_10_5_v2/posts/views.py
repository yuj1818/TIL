from django.shortcuts import render, redirect
from .forms import Form
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = Form()
    context={
        'form': form
    }
    return render(request, 'posts/form.html', context)
    
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user.is_authenticated:
        post.delete()
        return redirect('posts:index')
    else:
        return redirect('posts:detail', post.pk)

@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = Form(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/form.html', context)
