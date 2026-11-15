from django.db import models
from django.db.models.deletion import SET_NULL

from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class Department(BaseModel):
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name
        super().save(*args, **kwargs)

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = UserManager()

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=20,
                            choices=[("ADMIN", "Admin"), ("MANAGER", "Manager"), ("EMPLOYEE", "Employee")],
                            default="EMPLOYEE")
    clearance_level = models.IntegerField(choices=[(1, "PUBLIC"), (2, "INTERNAL"), (3, "CONFIDENTIAL")], default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
