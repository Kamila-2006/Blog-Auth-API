from rest_framework  import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Tag
from .serializers import TagSerializer
from .pagination import TagPagination


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]