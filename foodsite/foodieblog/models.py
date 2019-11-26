import datetime

from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    blog_post_category = models.CharField(max_length=50, blank=True)

    #meta
    class Meta:
        abstract = True

    #methods
    def __str__(self):
        return self.blog_post_category

#tuple choices to keep draft and published post separated when rendered out with templates.

STATUS = [
    ('d', 'Draft'), 
    ('p', 'Publish'),
    ('w', 'Withdrawn'),
]

class Post(BlogCategory):
    blog_title = models.CharField(max_length=200, unique=True, help_text='Enter Blog Title')
    slug = models.SlugField(max_length=200, unique=True)
    blog_author = models.ForeignKey(User,related_name='user_post', on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blog_content = models.TextField(help_text='Type Your Post Here')
    status = models.CharField(max_length= 1, choices=STATUS)

    def get_absolute_url(self):
        return reverse('posts_list',kwargs={'slug': self.slug})

    #to be tested to ensure post created will only posted recently not in future or past
    def was_posted_recently(self): 
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now 

      
    #meta
    class Meta:
        ordering = [ 'blog_author', '-created_on' ]

    #methods
    def __str__(self):
        return self.blog_title

    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, help_text='Your name')
    email = models.EmailField( blank=True, help_text='Your Email')
    body = models.TextField(help_text='Your comment')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def was_commented_recently(self): 
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now 
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'name': self.name})
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
