from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.title