from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_safe,
    require_POST,
    require_http_methods,
)
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse


@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.filter(org_comment__isnull=True)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment_form.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = Review.objects.get(pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            isLiked = False
        else:
            review.like_users.add(request.user)
            isLiked = True

        context = {
            'isLiked': isLiked,
            'countLike': review.like_users.count(),
        }
        
        return JsonResponse(context)
    return JsonResponse({'location': '/accounts/login/'}, status=302)

@require_POST
def re_comment(request, review_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('community:detail', review_pk)
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        re_comment = form.save(commit=False)
        re_comment.user = request.user
        re_comment.review = review
        re_comment.org_comment = comment
        form.save()
        return redirect('community:detail', review_pk)
    
@require_POST
def like_comment(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if comment.user != request.user:
            if comment.like_users.filter(pk=request.user.pk).exists():
                comment.like_users.remove(request.user)
                isLiked = False
            else:
                comment.like_users.add(request.user)
                isLiked = True
            context = {
                'isLiked': isLiked,
                'countLike': comment.like_users.count(),
            }

            return JsonResponse(context)
        return JsonResponse({'message':'본인의 댓글은 좋아요 누를 수 없음'}, status=403)
    return JsonResponse({'location': '/accounts/login/'}, status=302)