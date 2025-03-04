from django import forms
from .models import Task
from users.models import CustomUser

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=CustomUser.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    start_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'))
    end_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'), required=False)

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            # 'assigned_to': forms.Select(queryset=CustomUser.objects.all(), attrs={'class': 'form-control'}),
            'estimated_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_allocation': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget_used': forms.NumberInput(attrs={'class': 'form-control'}),
            'risk_level': forms.Select(attrs={'class': 'form-control'}),
            'milestone': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'workload': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError("End date must be after start date.")

        return cleaned_data