from django.urls import path
from .views import ProjectAPIView, ProjectDetailAPIView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, CustomLoginView, CustomLogoutView, DashboardView

urlpatterns = [
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('api/', ProjectAPIView.as_view(), name='project_api'),
    path('api/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail_api')
    # path('users/', UserListView.as_view(), name='user_list'),
    # path('user/create/', UserCreateView.as_view(), name='user_create'),
    # path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    # path('tasks/', TaskListView.as_view(), name='task_list'),
    # path('task/create/<int:project_id>/', TaskCreateView.as_view(), name='task_create'),
    # path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    # path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    # path('report/', ReportView.as_view(), name='project_report'),  # Reports page
    # path('budget/', BudgetView.as_view(), name='project_budget'),  # Budget page
]