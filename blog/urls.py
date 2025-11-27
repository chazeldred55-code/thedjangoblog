from django.urls import path
from .views import index, BlogListView

urlpatterns = [
    path('', index, name='index'),              # Homepage
    path('blog/', BlogListView.as_view(), name='blog'),  # Blog list page
]
