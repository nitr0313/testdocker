from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=80, blank=True, null=True)
    pass