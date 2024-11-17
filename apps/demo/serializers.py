# apps/demo/serializers.py
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)  # Include author's username

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)  # Count of comments
    user = serializers.CharField(source='user.username', read_only=True)  # Author's username
    comments = serializers.SerializerMethodField()  # Nested comments

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        # Fetch up to 3 latest comments, sorted by timestamp
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data
