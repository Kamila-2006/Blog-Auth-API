from rest_framework  import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Tag
from .serializers import TagSerializer
from posts.serializers import PostSerializer
from .pagination import TagPagination


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]

class TagPostsView(APIView):
    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        posts = tag.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)