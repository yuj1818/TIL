from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomCreationForm, CustomUserChangeForm, ProfileForm
from django.contrib.auth import update_session_auth_hash
from .models import User, Profile
from posts.models import Post
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        profile_form = ProfileForm()
        if form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile_form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def delete(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        return redirect('posts:index')
    else:
        return render(request, 'accounts/delete.html')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
        a = []
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

def profile(request, user_name):
    user = User.objects.get(username=user_name)
    profile = user.profile_set.get(user=user.id)
    posts = user.post_set.all()
    context = {
        'profile':profile,
        'posts':posts,
    }
    print(profile)
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            form.save()
            return redirect('profile', request.user)
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form':form,
    }
    return render(request, 'accounts/profile_update.html', context)