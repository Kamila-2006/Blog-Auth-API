from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from .models import Category
from .serializers import CategorySerializer
from .pagination import CategoryPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]