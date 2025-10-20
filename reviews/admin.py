from django.contrib import admin
from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "featured", "created_at")
    list_filter = ("featured", "created_at")
    search_fields = ("user__username", "content")
