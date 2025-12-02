from django.shortcuts import render
from django.views import generic
from .models import Post

# Homepage view → uses index.html
def index(request):
    latest_posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })

# Blog list view → uses blog.html (not index.html)
class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'   # Fixed
    context_object_name = 'posts'
    paginate_by = 6                    # Added pagination

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')