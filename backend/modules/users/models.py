from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    # BaseUserManager,
    # PermissionsMixin
)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=26, unique=True)
    is_active = models.BooleanField(default=True)
