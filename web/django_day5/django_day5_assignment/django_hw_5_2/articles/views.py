from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    data = Article.objects.all()
    context = {
        'articles': data,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    Article.objects.create(title=title, content=content)
    
    return redirect('index')