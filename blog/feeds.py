from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('home')
    description = 'Latests posts'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title
        
    def item_description(self, item):
        return truncatewords(item.synopsis, 30)