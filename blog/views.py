from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, slug):
    """
    Display a single published Post based on its slug.
    Demonstrates passing context to the template.
    """
    # Only get published posts
    queryset = Post.objects.filter(status=1)

    # Retrieve the post with matching slug or return 404
    post = get_object_or_404(queryset, slug=slug)

    # Context dictionary – passing data to template
    context = {
        "post": post,       # main post object
        "coder": "Your Name"  # example additional context
    }

    # Render template with context
    return render(
        request,
        "blog/post_detail.html",
        context
    )
