from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import Project 
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import ProjectSerializer
from .forms import ProjectForm 
import datetime
from django.shortcuts import get_object_or_404, render
class CustomLoginView(LoginView):
    template_name = 'project_tracker/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'project_tracker/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_admin'] = self.request.user.is_superuser
        context['projects'] = Project.objects.all() 
        return context

class ProjectListView(TemplateView):
    template_name = 'project_tracker/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_tracker/project_form.html'
    success_url = reverse_lazy('project_list')
    # def form_valid(self, form):
    #     # Convert date format from 'DD-MM-YYYY' to 'YYYY-MM-DD'
    #     form.instance.start_date = datetime.datetime.strptime(self.request.POST['start_date'], '%d-%m-%Y').date()
    #     form.instance.end_date = datetime.datetime.strptime(self.request.POST['end_date'], '%d-%m-%Y').date()
    #     return super().form_valid(form)
    def form_valid(self, form):
        # You can do custom actions before saving the form, such as logging
        return super().form_valid(form)

    def form_invalid(self, form):
        # You can log any issues if the form is invalid
        return render(self.request, self.template_name, {'form': form})

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_tracker/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_tracker/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

class ProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class UserCreateView(LoginRequiredMixin, CreateView):
#     model = CustomUser
#     form_class = UserForm
#     template_name = 'project_tracker/user_form.html'
#     success_url = reverse_lazy('user_list')
#     def form_valid(self, form):
#         # You can do custom actions before saving the form, such as logging
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         # You can log any issues if the form is invalid
#         return render(self.request, self.template_name, {'form': form})

# # List all users
# class UserListView(LoginRequiredMixin, ListView):
#     model = CustomUser
#     template_name = 'project_tracker/user_list.html'
#     context_object_name = 'users'

# # Update an existing user
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     model = CustomUser
#     form_class = UserForm
#     template_name = 'project_tracker/user_form.html'
#     success_url = reverse_lazy('user_list')

# # Delete a user
# class UserDeleteView(LoginRequiredMixin, DeleteView):
#     model = CustomUser
#     template_name = 'project_tracker/user_confirm_delete.html'
#     success_url = reverse_lazy('user_list')


    
# # Create a view for Reports page
# class ReportView(TemplateView):
#     template_name = 'project_tracker/reports.html'  # This will display reports

# # Create a view for Budget page
# class BudgetView(TemplateView):
#     template_name = 'project_tracker/budget.html'  # This will display the budget