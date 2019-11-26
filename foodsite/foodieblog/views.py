from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.views import View

from .models import Post, Comment

class PostList(generic.ListView):
    model = Post
    #post = get_object_or_404(Post, slug=slug)
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "posts_list"

    #to be tested to ensure only returns post that are lte the timezone.now
    def get_queryset(self):
        return Post.objects.filter(created_on__lte=timezone.now()).order_by('created_on')[:5]

