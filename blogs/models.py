import os
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


def blog_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    title_slug = slugify(instance.title)
    now = datetime.now()

    filename = f"{title_slug}-{now.strftime('%d%m%Y-%H%M%S')}.{ext}"

    return os.path.join(
        'blog_images',
        now.strftime('%Y'),
        now.strftime('%m'),
        filename
    )


STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    author = models.ForeignKey( User,
        on_delete=models.CASCADE
    )

    feature_image = models.ImageField(
        upload_to=blog_image_upload_path,
        blank=True,
        null=True
    )

    short_description = models.TextField()
    content = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Draft"
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment + " - " + self.blog.title + " - " + self.user.username