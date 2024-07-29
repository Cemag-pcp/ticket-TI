from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_engineer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, default='')  # Campo para o nome completo
    sector = models.CharField(max_length=255, default='')     # Campo para o setor