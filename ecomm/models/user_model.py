from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    uuid = models.CharField(max_length=32, editable=False, default=uuid4(), null=True, blank=True)

