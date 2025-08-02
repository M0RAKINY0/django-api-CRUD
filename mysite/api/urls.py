from django.urls import path
from . import views

urlpatterns = [
    path("blogPost/", views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
]