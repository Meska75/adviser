from django.utils import timezone
from django.shortcuts import render , get_object_or_404, redirect
from blog.models import Post , Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import datetime
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from blog.models import *
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
def blog_view(request, cat_name=None, author_username=None,date=None,tag_name=None):
    post = Post.objects.filter(published_date__lte=timezone.now(), published_status=1)
    latest_post = post.first()
    if cat_name:
        post = post.filter(category__name=cat_name,published_date__lte=timezone.now(), published_status=1)
    elif author_username:
        post = post.filter(author__username=author_username,published_date__lte=timezone.now(), published_status=1)
    elif date:
        raw_date = date.split()[0].split('T')[0]
        date = datetime.strptime(raw_date,"%Y-%m-%d")
        post = post.filter(published_date__date=date, published_status=1)
    elif tag_name:
        post = post.filter(tag__name__in=[tag_name],published_date__lte=timezone.now(), published_status=1)
    post = Paginator(post,3)       
    try:
        page_number = request.GET.get('page')
        post = post.get_page(page_number)
    except PageNotAnInteger:
        post = post.get_page(1)
    except EmptyPage:
        post = post.get_page(1)
    context = {'posts':post, 'latest_post':latest_post}
    return render(request, 'blog/blog.html',context)


def simple_blog_view(request, cat_name=None, author_username=None,date=None,tag_name=None):
    post = Post.objects.filter(published_date__lte=timezone.now(), published_status=1)
    if cat_name:
        post = post.filter(category__name=cat_name,published_date__lte=timezone.now(), published_status=1)
        reason = cat_name
    elif author_username:
        post = post.filter(author__username=author_username,published_date__lte=timezone.now(), published_status=1)
    elif date:
        raw_date = date.split()[0].split('T')[0]
        date = datetime.strptime(raw_date,"%Y-%m-%d")
        post = post.filter(published_date__date=date, published_status=1)
    elif tag_name:
        post = post.filter(tag__name__in=[tag_name],published_date__lte=timezone.now(), published_status=1)
    post = Paginator(post,3)       
    try:
        page_number = request.GET.get('page')
        post = post.get_page(page_number)
    except PageNotAnInteger:
        post = post.get_page(1)
    except EmptyPage:
        post = post.get_page(1)
    context = {'posts':post,}
    return render(request, 'blog/blog-simple-home.html',context)



def blogsingle_view(request, pid):
    base_query = Post.objects.filter(published_date__lte=timezone.now(), published_status=1)
    post = get_object_or_404(base_query, id=pid)

    author_posts_qs = Post.objects.filter(
        author=post.author,
        published_status=1,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    author_posts_count = author_posts_qs.count()

    if post.login_require and not request.user.is_authenticated:
        return redirect(f"{reverse('accounts:login')}?next={request.get_full_path()}")
    # === Handle POST (comment submission) ===
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # don't save yet

            # Get the 'post' sent from the form (could be a Post instance or an id)
            sent_post = form.cleaned_data.get('post')
            sent_post_id = None
            if hasattr(sent_post, 'id'):
                sent_post_id = sent_post.id
            else:
                try:
                    sent_post_id = int(sent_post)
                except Exception:
                    sent_post_id = None

            # If posted post id doesn't match current page's post, override (safe)
            if sent_post_id != post.id:
                # Option A (safe override): force assign to current post
                comment.post = post

                # Option B (strict): reject request if mismatch (uncomment to use)
                # messages.error(request, "Invalid post id submitted.")
                # return redirect('blog:blogsingle', pid=post.id)
            else:
                # If the form already set comment.post to an instance, keep it; otherwise use current post
                if hasattr(sent_post, 'id'):
                    comment.post = sent_post
                else:
                    comment.post = post

            # If user is authenticated, optionally override name/email
            if request.user.is_authenticated:
                comment.name = request.user.get_full_name() or request.user.username
                comment.email = request.user.email
            comment.save()
            messages.success(request, "Your comment has been submitted successfully.")
            # Redirect to avoid double post on refresh
            return redirect('blog:blogsingle', pid=post.id)
        else:
            # Form invalid — do NOT call form.save() => avoids ValueError
            # Log / print errors for debugging (dev only)
            if hasattr(request, 'session'):  # simple guard
                # print to console (development)
                print("CommentForm errors:", form.errors)
            messages.error(request, "There was a problem with your comment")
    else:
        # GET: prepare form, prefill name/email/post for authenticated users
        initial = {'post': post.id}
        if request.user.is_authenticated:
            initial['name'] = request.user.get_full_name() or request.user.username
            initial['email'] = request.user.email
        form = CommentForm(initial=initial)
    # === Comments and prev/next logic (unchanged) ===
    comments = Comment.objects.filter(post=post, approve=1).order_by('-created_date')
    all_posts = list(base_query)
    try:
        index = next(i for i, p in enumerate(all_posts) if p.pk == post.pk)
    except StopIteration:
        index = None
    previous_post = None
    next_post = None
    if index is not None:
        if index > 0:
            next_post = all_posts[index - 1]
        if index < len(all_posts) - 1:
            previous_post = all_posts[index + 1]
    context = {
        'post': post,
        'author_posts_count': author_posts_count,
        'prev_post': previous_post,
        'next_post': next_post,
        'comments': comments,
        'commentform': form,
    }
    post.counted_view += 1
    post.save()
    return render(request, 'blog/blog-sinlge.html', context)

    
def blog_search(request):
    post = Post.objects.filter(published_date__lte=timezone.now(), published_status=1)
    search_query = request.GET.get('search')
    
    if search_query:
        post = post.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        ).distinct()
    
    post = Paginator(post, 3)
    
    try:
        page_number = request.GET.get('page')
        post = post.get_page(page_number)
    except PageNotAnInteger:
        post = post.get_page(1)
    except EmptyPage:
        post = post.get_page(1)

    context = {
        'posts': post,
        'search_query': search_query  # برای نمایش در template
    }
    return render(request, 'blog/blog-simple-home.html', context)