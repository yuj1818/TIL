from django.shortcuts import render, redirect
from .forms import Form, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
    return redirect('posts:index')

@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user != post.author:
        return redirect('posts:index')
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

@require_POST
def comment_create(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('posts:index')
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            form.save()
            return redirect('posts:index')

@require_GET
@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:index')

@require_POST
def like(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('posts:index')
    
    post = Post.objects.get(pk=post_pk)
    if post.author != request.user:
        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
    return redirect('posts:index')

@login_required
def show_likes(request):
    User = get_user_model()
    user = User.objects.get(username=request.user)
    likes = user.like_posts.all()
    comment_form = CommentForm()
    context = {
        'likes': likes,
        'comment_form': comment_form,
    }
    return render(request, 'posts/likes.html', context)

@login_required
def show_followings(request):
    followings = request.user.followings.all()
    posts = Post.objects.filter(author__in=followings).order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/followings.html', context)