from django.db import models

from django.db import models

class StoreContact(models.Model):
    city = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=255)
    

    def __str__(self):
        return f"Contact for {self.city}"