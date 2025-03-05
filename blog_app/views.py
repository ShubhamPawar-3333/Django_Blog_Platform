# blog_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm, CommentForm
from analytics.models import PageView

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_app/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    PageView.objects.create(
        post=post,
        user=request.user if request.user.is_authenticated else None,
        ip_address=request.META.get('REMOTE_ADDR')
    )
    comments = post.comments.all() if request.user.is_authenticated else []
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog_app/blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog_app/create_post.html', {'form': form})