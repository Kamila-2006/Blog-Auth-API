from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from posts.serializers import PostSerializer
from .pagination import CategoryPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

class CategoryPostsView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        posts = category.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)