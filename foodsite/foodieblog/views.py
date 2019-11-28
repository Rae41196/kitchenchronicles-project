from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views import View

from .models import Post, Comment
from .form import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "posts_list"

    # #to be tested to ensure only returns post that are lte the timezone.now
    # def get_queryset(self):
    #     return Post.objects.filter(created_on__lte=timezone.now()).order_by('created_on')[:5]

def post_detail(request, slug):
    
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form
        }
    )
