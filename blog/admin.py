from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category, Vote, Profile


# ------------------------
# Comment inline for Post
# ------------------------
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'body', 'approved', 'created_on')
    readonly_fields = ('created_on',)
    ordering = ('-created_on',)


# ------------------------
# Post admin with Summernote and comments inline
# ------------------------
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    inlines = [CommentInline]


# ------------------------
# Comment admin
# ------------------------
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    ordering = ('-created_on',)


# ------------------------
# Register simple models
# ------------------------
admin.site.register(Category)
admin.site.register(Vote)
admin.site.register(Profile)
