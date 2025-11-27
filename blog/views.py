from django.shortcuts import render
from django.views import generic
from .models import Post

# Homepage view
def index(request):
    # Latest 3 published posts
    latest_posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts})

# Blog list page (all published posts)
class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')
