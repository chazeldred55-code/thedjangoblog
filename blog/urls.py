from django.urls import path
from .views import HomePageView, BlogListView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]