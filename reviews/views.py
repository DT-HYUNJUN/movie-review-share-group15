from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')


@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk) 
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


@login_required
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # 댓글기능 구현
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:index')
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)