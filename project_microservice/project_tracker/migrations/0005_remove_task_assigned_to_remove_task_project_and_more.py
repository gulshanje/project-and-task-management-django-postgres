# Generated by Django 5.1.6 on 2025-03-03 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0004_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
