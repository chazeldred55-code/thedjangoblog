from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    # Enable Summernote rich-text editor for the 'content' field
    summernote_fields = ('content',)
