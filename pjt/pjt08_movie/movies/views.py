from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    # 선택한 장르의 영화 리스트 중 popularity가 높은 것 상위 6개 추천
    selectedGenre = request.GET.get('selectedGenre')
    recommendedMovies = Movie.objects.filter(genres__name=selectedGenre).order_by('-popularity')[:6]
    context = {
        'recommendedMovies': recommendedMovies,
    }
    return render(request, 'movies/recommended.html', context)