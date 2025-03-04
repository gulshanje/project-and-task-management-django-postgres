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
  