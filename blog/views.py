from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

# Homepage view → uses index.html, paginated
class HomePageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


# Blog list view → optional list page
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


# --------------------------------------------------
# Function-Based View required by tutorial
# --------------------------------------------------
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post`` — an instance of :model:`blog.Post`.

    **Template:** :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )