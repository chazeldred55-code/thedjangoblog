from django.urls import path
from .views import HomePageView, BlogListView, post_detail

urlpatterns = [
    # Homepage
    path('', HomePageView.as_view(), name='home'),

    # Blog list page
    path('blog/', BlogListView.as_view(), name='blog_list'),

    # Single post detail page
    path('blog/<slug:slug>/', post_detail, name='post_detail'),
]
