from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Post status choices
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """Subreddit-style categories for posts"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post model for Reddit-style forum"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """Comment model for posts (threaded optional)"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies'
    )  # Optional threaded comments

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body[:20]} by {self.author}"


class Vote(models.Model):
    """Vote model to track upvotes and downvotes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=((1, 'Upvote'), (-1, 'Downvote')))

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} voted {self.value} on {self.post.title}"