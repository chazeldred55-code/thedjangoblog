from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField


# ------------------------
# Category model
# ------------------------
class Category(models.Model):
    """Subreddit-style categories for posts"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ------------------------
# Post model
# ------------------------
class Post(models.Model):
    """Post model for Reddit-style forum"""

    # Status constants
    DRAFT = 0
    PUBLISHED = 1
    STATUS_CHOICES = (
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    featured_image = CloudinaryField(
        "image",
        default="placeholder",
    )
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# ------------------------
# Comment model
# ------------------------
class Comment(models.Model):
    """Comment model for posts (supports threaded replies)"""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter",
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )

    class Meta:
        ordering = ["created_on"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment {self.body[:20]} by {self.author}"


# ------------------------
# Vote model
# ------------------------
class Vote(models.Model):
    """Vote model to track upvotes and downvotes"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    value = models.SmallIntegerField(
        choices=((1, "Upvote"), (-1, "Downvote")),
    )

    class Meta:
        unique_together = ("user", "post")
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return (
            f"{self.user} voted {self.value} "
            f"on {self.post.title}"
        )


# ------------------------
# Profile model
# ------------------------
class Profile(models.Model):
    """User profile with avatar and bio"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.CharField(
        max_length=255,
        default="images/no-profile-photo.png",
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
