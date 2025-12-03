from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Homepage view → uses index.html, paginated
class HomePageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'  # matches index.html loop
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


# Blog list view → optional, different template
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


# Post detail view → uses post_detail.html
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
