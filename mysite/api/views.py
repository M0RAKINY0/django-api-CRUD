from django.shortcuts import render, redirect
from rest_framework import generics,status
from rest_framework.response import Response
from.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView 
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages 
from .form import CustomerUserCreationForm, CustomerAuthenticationForm
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import response 
from rest_framework import status  

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete (self, request, *args, **kwargs):
        BlogPost.object.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogpostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)