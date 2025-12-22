from django.urls import path
from .views import BlogListView, post_detail, comment_edit, comment_delete

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("blog/", BlogListView.as_view(), name="blog_list"),

    path(
        "blog/<slug:slug>/comment/<int:comment_id>/edit/",
        comment_edit,
        name="comment_edit",
    ),
    path(
        "blog/<slug:slug>/comment/<int:comment_id>/delete/",
        comment_delete,
        name="comment_delete",
    ),

    path("blog/<slug:slug>/", post_detail, name="post_detail"),
]