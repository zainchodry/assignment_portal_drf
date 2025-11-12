from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_Choices = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]

    role = models.CharField(max_length=20, choices=Role_Choices)
