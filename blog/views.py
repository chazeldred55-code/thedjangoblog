from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import ListView

from .forms import CommentForm
from .models import Comment, Post


# -------------------------
# Blog list view (home page)
# -------------------------
class BlogListView(ListView):
    """
    Displays a list of all published blog posts on the home page.
    """
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return (
            Post.objects
            .filter(status=Post.PUBLISHED)
            .order_by("-created_on")
        )


# -------------------------
# Blog post detail view
# -------------------------
def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.PUBLISHED,
    )

    # Show approved comments to everyone,
    # plus the current user's own pending comments
    if request.user.is_authenticated:
        comments = post.comments.filter(
            Q(approved=True) | Q(author=request.user)
        ).order_by("-created_on")
    else:
        comments = post.comments.filter(
            approved=True
        ).order_by("-created_on")

    comment_count = post.comments.filter(
        approved=True
    ).count()

    if request.method == "POST":
        # Guard: Anonymous users cannot submit comments
        if not request.user.is_authenticated:
            messages.error(
                request,
                "Please log in to leave a comment.",
            )
            return HttpResponseRedirect(
                reverse("account_login")
            )

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            messages.success(
                request,
                "Comment submitted and awaiting approval.",
            )
            return HttpResponseRedirect(
                reverse(
                    "post_detail",
                    kwargs={"slug": slug},
                )
            )

        messages.error(request, "Error submitting comment.")
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }

    return render(
        request,
        "blog/post_detail.html",
        context,
    )


# -------------------------
# Edit a comment (owner-only)
# -------------------------
@login_required
def comment_edit(request, slug, comment_id):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.PUBLISHED,
    )

    # Security: ensure the comment belongs to this post
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post=post,
    )

    # Security: only the author can edit
    if comment.author != request.user:
        messages.error(
            request,
            "You can only edit your own comments.",
        )
        return HttpResponseRedirect(
            reverse(
                "post_detail",
                kwargs={"slug": slug},
            )
        )

    if request.method == "POST":
        comment_form = CommentForm(
            data=request.POST,
            instance=comment,
        )
        if comment_form.is_valid():
            edited = comment_form.save(commit=False)
            edited.post = post

            # Moderation choice: force re-approval after edits
            edited.approved = False

            edited.save()
            messages.success(
                request,
                "Comment updated and awaiting approval.",
            )
            return HttpResponseRedirect(
                reverse(
                    "post_detail",
                    kwargs={"slug": slug},
                )
            )

        messages.error(request, "Error updating comment.")
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


# -------------------------
# Delete a comment (owner-only)
# -------------------------
@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.PUBLISHED,
    )

    # Security: ensure the comment belongs to this post
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post=post,
    )

    # Security: only the author can delete
    if comment.author != request.user:
        messages.error(
            request,
            "You can only delete your own comments.",
        )
        return HttpResponseRedirect(
            reverse(
                "post_detail",
                kwargs={"slug": slug},
            )
        )

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted.")
        return HttpResponseRedirect(
            reverse(
                "post_detail",
                kwargs={"slug": slug},
            )
        )

    # GET -> show confirm page
    return render(
        request,
        "blog/comment_confirm_delete.html",
        {
            "post": post,
            "comment": comment,
        },
    )
