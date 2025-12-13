from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages

from .models import Post
from .forms import CommentForm


class BlogListView(ListView):
    """
    Displays a list of all published blog posts on the home page.
    """
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by("-created_on")


def post_detail(request, slug):
    """
    Display a single blog post and handle comment submission.
    Only published posts (status=1) are accessible.
    """

    # Get published post
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # Get comments related to the post
    comments = post.comments.all().order_by("-created_on")

    # Count approved comments
    comment_count = post.comments.filter(approved=True).count()

    # Handle comment submission
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            messages.success(
                request,
                "Comment submitted and awaiting approval"
            )

    # Empty form for GET request
    comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    return render(request, "blog/post_detail.html", context)