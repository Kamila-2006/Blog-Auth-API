from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'category', 'created_at', 'updated_at', 'status')
    search_fields = ('title', 'author', 'category', 'status')
    exclude = ('slug',)