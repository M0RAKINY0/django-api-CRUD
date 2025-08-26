from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permission import AllowAny
from rest_framework import status 
from .forms import CustomUserCreationForm, CustomAuthenticationForm 

@api_view (['GET', 'POST'])
@permission_classes([allowAny])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response ({'message': 'user created successfully '}, status = status.HTTP_201_CREATED)
        return (form.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'signup endpoint'})

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method =='POST':
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return Response({'message:' 'login successful!'}, status=ststus.HTTP_200_OK)
                return Response ({'error': 'invalid login credential'}, status=status.HTTP_400_BAD_REQUEST)
            return Response ({'details' : 'login endpoint'})

@api_view (['POST'])
def logout(request):
    logout(request)
    return Response ({'message': 'logout successful'}, status=status.HTTP_200_OK)