from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField()
    start_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'))
    end_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'), required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError("End date must be after start date.")

        return cleaned_data
    
# from django import forms
# from .models import Project 


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'description', 'start_date', 'end_date']

#         widgets = {
#             'start_date': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
#             'end_date': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(ProjectForm, self).__init__(*args, **kwargs)
#         self.fields['start_date'].input_formats = ['%d-%m-%Y']
#         self.fields['end_date'].input_formats = ['%d-%m-%Y']
    


# # class UserForm(UserCreationForm):
# #     email = forms.EmailField(required=True)
# #     designation = forms.ChoiceField(choices=CustomUser.DESIGNATION_CHOICES)  # Now it should work

# #     class Meta:
# #         model = CustomUser
# #         fields = ['username', 'email', 'password1', 'password2', 'designation']

# # class TaskForm(forms.ModelForm):
# #     start_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'))
# #     end_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%Y'), required=False)

# #     class Meta:
# #         model = Task
# #         fields = '__all__'
# #         widgets = {
# #             'project': forms.Select(attrs={'class': 'form-control'}),
# #             'task_name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'assigned_to': forms.Select(attrs={'class': 'form-control'}),
# #             'estimated_hours': forms.NumberInput(attrs={'class': 'form-control'}),
# #             'budget_allocation': forms.NumberInput(attrs={'class': 'form-control'}),
# #             'budget_used': forms.NumberInput(attrs={'class': 'form-control'}),
# #             'risk_level': forms.Select(attrs={'class': 'form-control'}),
# #             'milestone': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
# #             'comments': forms.Textarea(attrs={'class': 'form-control'}),
# #             'workload': forms.NumberInput(attrs={'class': 'form-control'}),
# #             'status': forms.Select(attrs={'class': 'form-control'}),
# #         }
    
# #     def __init__(self, *args, **kwargs):
# #         super(ProjectForm, self).__init__(*args, **kwargs)
# #         self.fields['start_date'].input_formats = ['%d-%m-%Y']
# #         self.fields['end_date'].input_formats = ['%d-%m-%Y']