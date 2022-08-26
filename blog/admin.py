from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'img', 'author','publish','status')
    list_filter = ('status','created', 'publish', 'author')
   
admin.site.register(Post, PostAdmin)