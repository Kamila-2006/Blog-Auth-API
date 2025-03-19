from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrAdmin
from .models import Post, PostLike
from .serializers import PostSerializer
from .pagination import PostPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        else:
            return [IsAuthorOrAdmin()]

class PostReactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        value = request.data.get("value")

        if value not in ["like", "dislike"]:
            return Response({"error": "Invalid value. Use 'like' or 'dislike'."}, status=400)

        like, created = PostLike.objects.get_or_create(user=request.user, post=post)

        if not created:
            if like.value == value:
                like.delete()
                return Response({"message": "Reaction removed"}, status=200)
            else:
                like.value = value
                like.save()
                return Response({"message": f"Reaction changed to {value}"}, status=200)

        return Response({"message": f"{value} added"}, status=201)