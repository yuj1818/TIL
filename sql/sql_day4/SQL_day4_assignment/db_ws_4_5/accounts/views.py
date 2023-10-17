from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, ChangeAuthorityForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import update_session_auth_hash, get_user_model

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('stores:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('stores:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('stores:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stores:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def show_members(request):
    User = get_user_model()
    members = User.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'accounts/members.html', context)

@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:show_members')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET', 'POST'])
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:show_members')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def change_authority(request, user_pk):
    if not request.user.is_superuser:
        return redirect('accounts:show_members')
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = ChangeAuthorityForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:show_members')
    else:
        form = ChangeAuthorityForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/change_authority.html', context)

def member_delete(request, user_pk):
    if not request.user.is_superuser:
        return redirect('accounts:show_members')
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    user.delete()
    return redirect('accounts:show_members')