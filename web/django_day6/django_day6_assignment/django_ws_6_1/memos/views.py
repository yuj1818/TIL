from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    memos = Memo.objects.all()
    context = {
        'memos': memos,
    }
    return render(request, 'memos/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            summary = form.cleaned_data['summary']
            memo = form.cleaned_data['memo']
            Memo.objects.create(summary=summary, memo=memo)
            return redirect('index')
    else:
        form = MemoForm()
    context = {
        'form': form,
    }
    return render(request, 'memos/create.html', context)

@require_http_methods(["GET"])
def detail(request, memo_pk):
    memo = get_object_or_404(Memo, pk=memo_pk)
    context = {
        'memo': memo,
    }
    return render(request, 'memos/detail.html', context)

@require_http_methods(["GET"])
def delete(request, memo_pk):
    memo = Memo.objects.get(pk=memo_pk)
    memo.delete()
    return redirect('index')