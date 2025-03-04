from django.test import TestCase
from .models import Project
from django.contrib.auth import get_user_model

class ProjectTestCase(TestCase):
    def test_create_project(self):
        project = Project.objects.create(name="Test Project", description="Test Desc", start_date="2024-01-01", end_date="2024-12-31")
        self.assertEqual(project.name, "Test Project")


class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
            designation="QA Specialist"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.check_password("password123"))