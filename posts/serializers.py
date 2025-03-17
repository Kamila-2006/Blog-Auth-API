from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'featured_image']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']