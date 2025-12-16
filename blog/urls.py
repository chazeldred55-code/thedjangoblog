from django.urls import path
from .views import BlogListView, post_detail, comment_edit, comment_delete

urlpatterns = [
    # Homepage shows list of published posts
    path("", BlogListView.as_view(), name="home"),

    # Optional dedicated blog list page
    path("blog/", BlogListView.as_view(), name="blog_list"),

    # Edit comment (must be before post_detail)
    path(
        "blog/<slug:slug>/comment/<int:comment_id>/edit/",
        comment_edit,
        name="comment_edit",
    ),

    # Delete comment (must be before post_detail)
    path(
        "blog/<slug:slug>/comment/<int:comment_id>/delete/",
        comment_delete,
        name="comment_delete",
    ),

    # Single post detail page (keep last)
    path("blog/<slug:slug>/", post_detail, name="post_detail"),
]
