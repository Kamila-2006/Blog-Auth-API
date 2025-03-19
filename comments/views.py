from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .pagination import CommentPagination
from rest_framework.response import Response


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user == comment.author or request.user == comment.post.author or request.user.is_staff:
            self.perform_destroy(comment)
            return Response({"message": "Comment deleted successfully"})
        return Response({"error": "You don't have permission to delete this comment"}, status=403)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user == comment.author:
            return super().update(request, *args, **kwargs)
        return Response({"error": "You don't have permission to edit this comment"}, status=403)