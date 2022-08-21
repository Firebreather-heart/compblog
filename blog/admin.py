from django.contrib import admin
from .models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'img', 'author','publish','status')
    list_filter = ('status','created', 'publish', 'author')
   
admin.site.register(Post, PostAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')