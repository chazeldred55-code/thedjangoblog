from django.contrib import admin
from django.urls import path, include  # include allows app-level URL routing

urlpatterns = [
    path('admin/', admin.site.urls),   # Django admin
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),    # All blog-related routes handled in blog/urls.py
]