from rest_framework import serializers
from blog.models import Post, Comment
from rest_framework.authentication import BasicAuthentication



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
        

    def get_comments(self, obj):
        ordered_comments = obj.comments.all().order_by('created')
        return CommentSerializer(ordered_comments, many=True).data



