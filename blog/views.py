from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from blog.models import Post, Comment

class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_posts"
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class PostView(generic.DetailView):
    model = Post
    template_name = "blog/post.html"
    slug_field = 'slug'
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())
