from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.title
