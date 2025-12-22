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
    paginate_by = 6  # optional but supported by template

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by("-created_on")


def post_detail(request, slug):
    """
    Display a single blog post and handle comment submission.
    """
    post = get_object_or_404(Post, slug=slug, status=1)
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
            return HttpResponseRedirect(
                reverse("post_detail", kwargs={"slug": slug})
            )
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
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, "You can only edit your own comments!")
        return HttpResponseRedirect(
            reverse("post_detail", kwargs={"slug": slug})
        )

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, "Comment updated!")
            return HttpResponseRedirect(
                reverse("post_detail", kwargs={"slug": slug})
            )
        else:
            messages.error(request, "Error updating comment!")
    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        "blog/comment_edit.html",
        {
            "post": post,
            "comment": comment,
            "comment_form": comment_form,
        },
    )


def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error(request, "You can only delete your own comments!")
        return HttpResponseRedirect(
            reverse("post_detail", kwargs={"slug": slug})
        )

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted!")

    return HttpResponseRedirect(
        reverse("post_detail", kwargs={"slug": slug})
    )
