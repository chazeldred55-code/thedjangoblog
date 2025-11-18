# thedjangoblog/urls.py

from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # Import views from your blog app

urlpatterns = [
    path('admin/', admin.site.urls),    # Django admin
    path('', blog_views.index, name='index'),  # Home page: calls blog/views.py index()
]
