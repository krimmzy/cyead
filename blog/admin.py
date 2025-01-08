from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)