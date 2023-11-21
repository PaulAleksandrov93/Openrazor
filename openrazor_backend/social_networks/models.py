from django.db import models

class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, unique=True)
    link = models.URLField()

    def __str__(self):
        return self.name