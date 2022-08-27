from rest_framework import serializers
from blog.models import Post 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title','id', 'img', 'author','publish','status', 'synopsis',
                    'content', 'category','published',)
        model = Post