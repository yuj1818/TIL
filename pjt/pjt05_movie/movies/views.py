from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import MovieForm, CommentForm
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required

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