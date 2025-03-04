from django.test import TestCase
from .models import Project


class ProjectTestCase(TestCase):
    def test_create_project(self):
        project = Project.objects.create(name="Test Project", description="Test Desc", start_date="2024-01-01", end_date="2024-12-31")
        self.assertEqual(project.name, "Test Project")

