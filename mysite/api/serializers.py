#json = js object notation
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]