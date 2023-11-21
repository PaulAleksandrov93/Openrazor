from django.contrib import admin
from .models import StoreContact

@admin.register(StoreContact)
class StoreContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'phone', 'email', 'working_hours')