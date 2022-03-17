from django.shortcuts import render
from blog.models import Post,PostView,Like,Comment,Category
from blog.serializers import PostSerializer,LikeSerializer,CommentSerializer,PostViewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class PostListView(generics.ListAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        post = self.kwargs['post'].replace(("-"), (" "))
        return Post.objects.filter(post_name__title=post)


# Create your views here.
