from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Post, Comment
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
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

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
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        else:
            messages.error(request, "Error submitting comment!")
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    return render(request, "blog/post_detail.html", context)


def comment_edit(request, slug, comment_id):
    """
    View to edit an existing comment.
    Handles POST to update the comment and GET to prefill the form.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Only the comment author can edit
    if comment.author != request.user:
        messages.error(request, "You can only edit your own comments!")
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Require re-approval
            comment.save()
            messages.success(request, "Comment updated!")
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        else:
            messages.error(request, "Error updating comment!")
    else:
        # Prefill the form for editing
        comment_form = CommentForm(instance=comment)

    context = {
        "post": post,
        "comment_form": comment_form,
        "comment": comment,
    }

    return render(request, "blog/comment_edit.html", context)


def comment_delete(request, slug, comment_id):
    """
    View to delete an existing comment.
    Only allows POST requests to prevent accidental deletion.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, "You can only delete your own comments!")
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "Invalid request method for deleting comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))