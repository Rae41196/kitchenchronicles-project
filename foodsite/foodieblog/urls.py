from django.urls import path

from foodieblog import views
from .views import PostList

app_name='foodieblog'
urlpatterns =[
    path('', views.PostList.as_view(), name='index'),
    # path('<slug:slug>/', views.DetailsView.as_view())
]