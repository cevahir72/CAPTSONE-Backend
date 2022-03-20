from django.shortcuts import render
from blog.models import Post
from blog.serializers import PostSerializer,LikeSerializer,CommentSerializer,PostViewSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .permissions import IsStuffOrReadOnly



class PostListView(generics.ListAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class DetailView(generics.ListAPIView):
    queryset=Post.objects.all()
    serilizer_class = PostSerializer
    permission_classes = (IsStuffOrReadOnly,)



