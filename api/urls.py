from . import views 
from django.urls import path 




urlpatterns = [
    #path('', PostList.as_view(), ),
    #path('<uuid:pk>/', PostDetail.as_view(), ),
    # path('tag/<slug:tag_slug>/',views.post_list,),
    # path('feeds/', views.LatestPostsFeed(), ),
    # path('search/', views.search, )
    path('',views.post_list, name='home')
]