from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'designation', 'first_name', 'last_name', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match"
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.instance.pk is None: # only applies to creation
            password = self.cleaned_data.get("password1", user.username + "123") #if password1 is empty use default
        else:
            password = self.cleaned_data["password1"]

        user.set_password(password)

        if commit:
            user.save()
        return user