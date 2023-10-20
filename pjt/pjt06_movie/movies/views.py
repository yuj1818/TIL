from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import MovieForm, CommentForm
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_GET
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': movie.comment_set.filter(org_comment__isnull=True),
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if movie.user != request.user:
        return redirect('movies:detail', movie_pk)
    if request.method == 'POST':
        form =  MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie_pk': movie_pk,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if movie.user == request.user:
            movie.delete()
    return redirect('movies:detail', movie_pk)

@require_POST
def comments_create(request, movie_pk):
    if not request.user.is_authenticated:
        return redirect('movies:detail', movie_pk)
    movie = Movie.objects.get(pk=movie_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        form.save()
        return redirect('movies:detail', movie_pk)

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('movies:detail', movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)

@require_POST
def likes(request, movie_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    movie = Movie.objects.get(pk=movie_pk)
    if request.user != movie.user:
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
    return redirect('movies:index')

@require_GET
def like_movie_list(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    context = {
        'user': user,
    }
    return render(request, 'movies/like_movies.html', context)

@require_POST
def re_comment(request, movie_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('movies:detail', movie_pk)
    movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        re_comment = form.save(commit=False)
        re_comment.user = request.user
        re_comment.movie = movie
        re_comment.org_comment = comment
        form.save()
        return redirect('movies:detail', movie_pk)
    
@require_POST
def re_comment_delete(request, movie_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('movies:detail', movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)