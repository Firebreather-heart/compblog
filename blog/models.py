from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid 
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
# Create your models here.

class UUIDTaggedItem(GenericUUIDTaggedItemBase,TaggedItemBase):

    class Meta:
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'), ('published','Published'))

    CATEGORY_CHOICES =(('news','News'),('tech','Tech'),('lifestyle','Lifestyle'),
                            ('entertainment','Entertainment'),
                            ('fashion','Fashion'),('career','career'),
                            ('general','General'))
                            
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now, )
    updated = models.DateTimeField(default=timezone.now, )
    img = models.ImageField(upload_to='blog/images', blank=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')
    synopsis = models.CharField(max_length=250, blank=True)
    objects = models.Manager()
    published = PublishedManager()
    content = HTMLField(blank=True)
    category =  models.CharField(choices=CATEGORY_CHOICES, max_length=20, default='general')
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

class Subscribers(models.Model):
    mail = models.EmailField()
    joined = models.DateTimeField(auto_now_add=True)

    def get_queryset(self):
        return self.objects.filter('-joined')

class Msg(models.Model):
    email = models.EmailField()
    msg = models.CharField(max_length=1000)