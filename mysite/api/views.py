from django.shortcuts import render
from rest_framework import generics
from.models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIview):
    queryset = BlogPost.objectsall()
    serializer_class = BlogPostSerializer

class BlogpostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIview):
    queryset = BlogPost.objectsall()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"