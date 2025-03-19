from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'featured_image']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = {
            'id': instance.author.id,
            'username': instance.author.username,
            'first_name': instance.author.first_name,
            'last_name': instance.author.first_name,
        }
        representation['category'] = {
            'id': instance.category.id,
            'name': instance.category.name,
            'slug': instance.category.slug
        }
        representation['tags'] = [
            {
                'id': tag.id,
                'name': tag.name,
                'slug': tag.slug
            }
            for tag in instance.tags.all()
        ]
        return representation