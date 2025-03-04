from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from .forms import TaskForm
from .models import Project, Task
from project_tracker.models import Project
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project_tracker/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.kwargs.get('project_id')
        if project_id:
            initial['project'] = get_object_or_404(Project, pk=project_id)
        return initial
    
    def form_valid(self, form):
        # You can do custom actions before saving the form, such as logging
        return super().form_valid(form)

    def form_invalid(self, form):
        # You can log any issues if the form is invalid
        return render(self.request, self.template_name, {'form': form})

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'project_tracker/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'project_tracker/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

class TaskListView(ListView):
    model = Task
    template_name = 'project_tracker/task_list.html'
    context_object_name = 'tasks'
