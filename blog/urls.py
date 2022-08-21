from django.urls import path 
from . import views,feeds 



urlpatterns = [ 
    path('', views.post_list, name='home'),
    path('<uuid:pk>/', views.post_detail, name='detail'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('feeds/', feeds.LatestPostsFeed(), name='feeds'),
    path('search/', views.search, name='search')
]