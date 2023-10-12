from django.shortcuts import render, redirect
from .forms import TodoForm
from django.views.decorators.http import require_GET, require_http_methods
from .models import Todo

@require_GET
def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login')

@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)