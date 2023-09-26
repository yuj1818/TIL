from django.shortcuts import render, redirect, get_object_or_404
from .models import travels
from .forms import Form
from django.views.decorators.http import require_GET, require_POST, require_http_methods

# Create your views here.
@require_GET
def index(request):
    articles = travels.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'travels/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('detail', article.pk)
    else:
        form = Form()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)
    

@require_GET
def detail(request, article_pk):
    article = get_object_or_404(travels, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'travels/detail.html', context)