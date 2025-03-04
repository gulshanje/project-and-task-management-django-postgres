from django.db import models
from users.models import CustomUser  
from project_tracker.models import Project

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(CustomUser  , on_delete=models.SET_NULL, null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)
    budget_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    RISK_LEVEL_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES, default='Low')
    milestone = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    workload = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    STATUS_CHOICES = [
        ('NOT STARTED', 'NOT STARTED'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('ON HOLD', 'ON HOLD'),
        ('COMPLETED', 'COMPLETED'),
        ('OVERDUE', 'OVERDUE'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT STARTED')

    def __str__(self):
        return self.task_name