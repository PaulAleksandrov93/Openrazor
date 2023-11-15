from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    on_sale = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    recommended_products = models.ManyToManyField('self', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
