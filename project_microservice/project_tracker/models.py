from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
# class CustomUser(AbstractUser, PermissionsMixin):
#     DESIGNATION_CHOICES = [
#         ('Project Manager', 'Project Manager'),
#         ('UI/UX Designer', 'UI/UX Designer'),
#         ('Backend Designer', 'Backend Designer'),
#         ('Frontend Designer', 'Frontend Designer'),
#         ('Machine Learning Engineer', 'Machine Learning Engineer'),
#         ('QA Specialist', 'QA Specialist'),
#         ('DevOps Engineer', 'DevOps Engineer'),
#     ]

#     email = models.EmailField(unique=True)
#     designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

#     # Fix related_name conflicts
#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="customuser_set",
#         blank=True,
#         help_text="The groups this user belongs to."
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="customuser_permissions_set",
#         blank=True,
#         help_text="Specific permissions for this user."
#     )

#     def __str__(self):
#         return self.username
    

# class Task(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     task_name = models.CharField(max_length=255)
#     assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#     budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)
#     budget_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     RISK_LEVEL_CHOICES = [
#         ('Low', 'Low'),
#         ('Medium', 'Medium'),
#         ('High', 'High'),
#         ('Urgent', 'Urgent'),
#     ]
#     risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES, default='Low')
#     milestone = models.BooleanField(default=False)
#     comments = models.TextField(blank=True, null=True)
#     workload = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     STATUS_CHOICES = [
#         ('NOT STARTED', 'NOT STARTED'),
#         ('IN PROGRESS', 'IN PROGRESS'),
#         ('ON HOLD', 'ON HOLD'),
#         ('COMPLETED', 'COMPLETED'),
#         ('OVERDUE', 'OVERDUE'),
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT STARTED')

#     def __str__(self):
#         return self.task_name