from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User

class CustomUser(AbstractUser, PermissionsMixin):
    DESIGNATION_CHOICES = [
        ('Project Manager', 'Project Manager'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Backend Designer', 'Backend Designer'),
        ('Frontend Designer', 'Frontend Designer'),
        ('Machine Learning Engineer', 'Machine Learning Engineer'),
        ('QA Specialist', 'QA Specialist'),
        ('DevOps Engineer', 'DevOps Engineer'),
    ]

    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

    # Fix related_name conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return self.username
