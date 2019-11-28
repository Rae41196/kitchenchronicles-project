from django.urls import path

# from foodieblog import views
from foodieblog.views import PostList, post_detail 

# app_name='foodieblog'
urlpatterns =[
    path('', PostList.as_view(), name='index'),
    path('<slug:slug>/', post_detail, name='post_detail')
]