from django.urls import path
from .views import BlogListView, post_detail

urlpatterns = [
    # Homepage shows list of published posts
    path("", BlogListView.as_view(), name="home"),

    # Optional dedicated blog list page (can be same as home)
    path("blog/", BlogListView.as_view(), name="blog_list"),

    # Single post detail page
    path("blog/<slug:slug>/", post_detail, name="post_detail"),
]
