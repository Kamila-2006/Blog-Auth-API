from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['post'] = {
            'id': instance.post.id,
            'title': instance.post.title,
            'slug': instance.post.slug
        }

        representation['author'] = {
            'id': instance.author.id,
            'username': instance.author.username,
            'first_name': instance.author.first_name,
            'last_name': instance.author.first_name,
        }

        return representation