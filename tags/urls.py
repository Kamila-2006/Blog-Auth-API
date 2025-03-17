from django.urls import path
from . import views


urlpatterns = [
    path('', views.TagListCreateView.as_view(), name='tag-list'),
    path('<int:pk>/posts/', views.TagPostsView.as_view(), name='tag-posts'),
]