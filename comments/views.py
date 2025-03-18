from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from .pagination import CommentPagination