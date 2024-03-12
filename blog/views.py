from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

from blog.models import Post, Comment
from blog.forms import PostForm

class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "latest_posts"
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    def get(self, request, *args, **kwargs):
        if not request.path.endswith('/blog/'):
            return redirect(reverse_lazy('blog:index'))
        else:
            return render(request, self.template_name, {'latest_posts': self.get_queryset()})
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        if post_id:
            post_to_delete = get_object_or_404(Post, id=post_id)
            post_to_delete.delete()
        return redirect(reverse_lazy('blog:index'))
    

class PostView(generic.DetailView):
    model = Post
    template_name = "blog/post.html"
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class PostDeleteView(generic.DetailView):
    model = Post
    template_name = "blog/post_confirm_delete.html"

class SearchView(generic.ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "results"
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.none()

class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

class ContactView(generic.TemplateView):
    template_name = "blog/contact.html"

def make_a_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.pub_date = timezone.now()
        post.save()

    context = {'form': form}
    return render(request, 'blog/make_post.html', context)

