from django import template
from blog.models import Post , Category , Comment
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-polularposts.html')
def popular_posts():
    posts = Post.objects.filter(published_date__lte=timezone.now(), published_status=1).order_by('-counted_view')[:4]
    return {'popularposts':posts}

@register.inclusion_tag('blog/blog-category.html')
def post_categories():
    posts = Post.objects.filter(published_date__lte=timezone.now(), published_status=1).order_by('-published_date')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()       
    sorted_cat = sorted(cat_dict.items(), key=lambda item: item[1], reverse=True)
    return {'categories':dict(sorted_cat)}

@register.inclusion_tag('blog/blog-toptags.html')
def top_tags(limit=10):
    posts = Post.objects.filter(published_date__lte=timezone.now(), published_status=1)
    tag_dict = {}
    for post in posts:
        for tag in post.tag.all():
            tag_dict[tag] = tag_dict.get(tag, 0) + 1
    sorted_tags = sorted(tag_dict.items(), key=lambda x: x[1], reverse=True)
    return {'tags': dict(sorted_tags[:limit])}