from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise valueError("Email is required ")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    
    def CustomUser(AbstractUser, permissionsMixin):
        email = models.EmailField(unique=True)
        username = models.CharField(max_length=100, unique=True)
        is_active = models.booleanField(default=True)
        is_staff = models.booleanfield(default = False)
        date_joined = models.DateTimeField(auto_now_add=True)

        objects = CustomUserManager()


        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = ["username"]

        def __str__(self):
            return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title 

