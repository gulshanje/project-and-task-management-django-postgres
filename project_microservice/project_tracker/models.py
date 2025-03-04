from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
