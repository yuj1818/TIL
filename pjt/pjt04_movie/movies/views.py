from django.shortcuts import render, redirect
from .models import Movie
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_GET
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    # print(movie.movie_image)
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    # 글 작성자가 아닌데 수정 url로 접속 시도 시, 차단
    if request.user != movie.author:
        return redirect('movies:detail', pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('accounts:login')