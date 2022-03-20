from rest_framework import serializers
from blog.models import Category,Post, PostView,Comment,Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
        
class CommentSerializer(serializers.ModelSerializer):
    post_id =serializers.IntegerField(write_only=True, required=False)
    user_id =serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Comment
        fields = ("content","post_id","user_id",)

class LikeSerializer(serializers.ModelSerializer):
    post_id =serializers.IntegerField(write_only=True, required=False)
    user_id =serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model= Like
        fields = ("post_id", "user_id" , )
        
class PostViewSerializer(serializers.ModelSerializer):
    post_id =serializers.IntegerField(write_only=True, required=False)
    user_id =serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model= PostView
        fields = ("post_id", "user_id" , )
        
class PostSerializer(serializers.ModelSerializer):
    categories= CategorySerializer(many=True, write_only=True)
    comments = CommentSerializer (many=True, write_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model= Post
        fields = ("id","categories", "comments","comment_count","like_count", "image","publish_date","last_updated")
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_like_count(self, obj):
        return obj.like.count()
    

        

    
    
    
        
