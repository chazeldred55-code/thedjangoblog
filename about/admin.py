from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.
    Enables Summernote rich-text editor for content.
    """
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for CollaborateRequest model.
    Displays key fields in the admin list view.
    """
    list_display = ('message', 'read')
