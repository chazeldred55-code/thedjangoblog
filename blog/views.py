from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    """
    Displays a list of all published blog posts on the home page.
    """
    model = Post
    template_name = "blog/index.html"        # HTML template to render
    context_object_name = "posts"            # variable name in template

    def get_queryset(self):
        # Only return published posts (status=1)
        return Post.objects.filter(status=1).order_by("-created_on")


def post_detail(request, slug):
    """
    Display a single blog post based on its slug.
    Only published posts (status=1) are accessible.
    """

    # Filter only published posts
    queryset = Post.objects.filter(status=1)

    # Fetch post or return 404 if not found
    post = get_object_or_404(queryset, slug=slug)

    # Data passed into template
    context = {
        "post": post,
        "coder": "Your Name",   # example extra context
    }

    return render(request, "blog/post_detail.html", context)