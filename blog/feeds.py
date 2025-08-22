
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone

class LatestEntriesFeed(Feed):
    title = "recently blog posts"
    link = "/rss/feed/"  # بهتر است با اسلش شروع شود
    description = "best blog content"

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now(), published_status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:200]

    # افزودن متد جدید برای تعیین لینک هر آیتم
    def item_link(self, item):
        return reverse('blog:blogsingle', args=[str(item.id)])