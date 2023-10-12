from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentForm
from .models import Question, Comment
from random import choice

def index(request):
    questions = Question.objects.all()
    context = {
        'questions':questions,
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.id)
    else:
        form = QuestionForm()
    context = {
        'form':form,
    }
    return render(request, 'eithers/create.html', context)

def random(request):
    id_list = Question.objects.values_list('id', flat=True)
    chosen = choice(id_list)
    return redirect('eithers:detail', chosen)

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comments = question.comment_set.all()
    comment_form = CommentForm()
    context = {
        'question':question,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'eithers/detail.html', context)


def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.question = question
        form.save()
    return redirect('eithers:detail', question_pk)