from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'description', 'is_featured', 'slug']
    search_fields = ['name', 'description']
    list_filter = ['is_featured', 'parent']