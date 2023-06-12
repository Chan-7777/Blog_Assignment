# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/blogposts/', views.BlogPostListCreateAPIView.as_view(), name='blogpost-list-create'),
    path('api/blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blogpost-detail'),
]
