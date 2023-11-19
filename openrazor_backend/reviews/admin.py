from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'rating', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('user__username', 'product__name')