from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationform, AuthenticationForm

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "password1", "password2")

    class CustomAuthenticationForm(AuthenticationForm):
        username = forms.EmailField(label="Email")