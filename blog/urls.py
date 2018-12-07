from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('posts',posts_list,name="posts_all"),
    path('posts/<str:slug>/',PostDetail.as_view(),name="post_detail_url"),
    path('tags/',tags_list,name='tags_list_url'),
    path('tags/create',TagCreate.as_view(), name='tag_create_url'), 
    path('tag/<str:slug>/',TagDetail.as_view(),name="tag_detail_url")
]