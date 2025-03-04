from django.urls import path
from .views import   TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/<int:project_id>/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    
]