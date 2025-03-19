from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<slug:slug>/like/', views.PostReactionView.as_view(), name='reaction'),
    path('users/<str:username>/posts/', views.UserPostsView.as_view(), name='user-posts'),
]