from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListAPI.as_view()),
    path('post/draft/', views.PostDraftListAPI.as_view()),
    path('post/<int:pk>/', views.PostDetailAPI.as_view()),
    path('comment/', views.CommentAPI.as_view()),
    path('comment/<int:pk>/', views.CommentAPI.as_view()),
    path('api-token-auth/login/', views.LoginAPI.as_view()),
]