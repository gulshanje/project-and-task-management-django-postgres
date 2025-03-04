from django.urls import path
from .views import ProjectAPIView, ProjectDetailAPIView, ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, CustomLoginView, CustomLogoutView, DashboardView

urlpatterns = [
 
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('api/', ProjectAPIView.as_view(), name='project_api'),
    path('api/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail_api')
    
]