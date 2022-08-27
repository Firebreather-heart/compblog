#from rest_framework import viewsets 
from blog.models import Post 
from .serializers import PostSerializer 
# from django.shortcuts import get_object_or_404
# from django.contrib.syndication.views import Feed
# from django.template.defaultfilters import truncatewords
# from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger 
# from taggit.models import Tag
# from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank
# from django.db.models import Count
# from blog.forms import SearchForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


# class PostViewset(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer

# class LatestPostsFeed(Feed):
#     title = 'My blog'
#     link = reverse_lazy('home')
#     description = 'New posts of my blog.'
#     def items(self):
#         return Post.published.all()[:10]
#     def item_title(self, item):
#         return item.title
#     def item_description(self, item):
#         return truncatewords(item.body, 30)

@swagger_auto_schema(method='GET', )
@api_view(['GET'])
def post_list(request,):
    if request.method == 'GET':
        object_list = Post.objects.all()
        serialized_posts = PostSerializer(object_list, many=True)
        return Response(serialized_posts.data, status = status.HTTP_200_OK)
    else:
        return Response(serialized_posts.errors, status = status.HTTP_400_BAD_REQUEST)

# def post_detail(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post_tags_ids = post.tags.values_list('id', flat=True).exclude(id=pk)
#     similar_posts = Post.published.filter(tags__in=post_tags_ids)
#     similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:5]
#     return JsonResponse({'post':post,
#                         'similar_posts':similar_posts})

# def search(request):
#     form = SearchForm()
#     query = None 
#     results = []
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         query = request.GET.get('query')
#         #query = form.cleaned_data['query']
#         search_vector = SearchVector('title','content')
#         search_query =  SearchQuery(query) 
#         results = Post.published.annotate(search= search_vector,
#                                             rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
#     return JsonResponse({'form':form,
#                         'query':query,
#                         'results':results})