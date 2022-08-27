from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger 
from taggit.models import Tag
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank
from django.db.models import Count
# Create your views here.


def post_list(request,tag_slug=None):
    if request.method == 'GET':
        object_list = Post.published.all()
        tag_slug=None
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_list = object_list.filter(tags__in=[tag])
        paginator = Paginator(object_list, 6) 
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    return render(request,
                    'pbt/index.html',
                    {'page': page,
                    'posts': posts,
                    'tags':tag,
                    'obj':object_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    post_tags_ids = post.tags.values_list('id', flat=True).exclude(id=pk)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:5]
    return render(request, 'pbt/single.html',
                                {'post':post,
                                'comments':comments,
                                'similar_posts':similar_posts})
                            

def search(request):
    form = SearchForm()
    query = None 
    results = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        query = request.GET.get('query')
        #query = form.cleaned_data['query']
        search_vector = SearchVector('title','content')
        search_query =  SearchQuery(query) 
        results = Post.published.annotate(search= search_vector,
                                            rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
    return render(request, 'pbt/search.html',
                        {'form':form,
                        'query':query,
                        'results':results})