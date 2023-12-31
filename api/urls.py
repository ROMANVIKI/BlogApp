from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comments/<pk>', views.CommentDetailView.as_view(), name='comment_detail'),
]
