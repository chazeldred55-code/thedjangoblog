from django.urls import path
from .views import HomePageView, BlogListView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),                  # homepage
    path('blog/', BlogListView.as_view(), name='blog_list'),        # optional blog page
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # individual post
]