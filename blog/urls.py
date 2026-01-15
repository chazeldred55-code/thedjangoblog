from django.urls import path
from .views import BlogListView, post_detail, comment_edit, comment_delete

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_home"),

    # Comment actions (more specific) must come before the generic slug route
    path("<slug:slug>/comment/<int:comment_id>/edit/", comment_edit, name="comment_edit"),
    path("<slug:slug>/comment/<int:comment_id>/delete/", comment_delete, name="comment_delete"),

    # Post detail (generic)
    path("<slug:slug>/", post_detail, name="post_detail"),
]