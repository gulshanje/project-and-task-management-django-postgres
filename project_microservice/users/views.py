from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import CustomUserForm
from.models import CustomUser
class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'project_tracker/user_form.html'
    success_url = reverse_lazy('user_list')
    def form_valid(self, form):
        # You can do custom actions before saving the form, such as logging
        return super().form_valid(form)

    def form_invalid(self, form):
        # You can log any issues if the form is invalid
        return render(self.request, self.template_name, {'form': form})

# List all users
class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'project_tracker/user_list.html'
    context_object_name = 'users'

# Update an existing user
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'project_tracker/user_form.html'
    success_url = reverse_lazy('user_list')

# Delete a user
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'project_tracker/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


