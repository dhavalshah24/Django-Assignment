from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 250, unique_for_date = "publish")
    publish = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blog_posts")
    content = models.TextField()

    def get_absolute_url(self) :
        return reverse("blog:post_single", args = [self.slug])
    
    def get_author_url(self) :
        return reverse("blog:author", kwargs = {"author": self.author})

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title