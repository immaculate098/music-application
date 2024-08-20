from django import forms
from .models import Signup, Login
# from django.contrib.auth.hashers import check_password

class SignupForm(forms.ModelForm):
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Signup
        fields = ['username', 'email', 'password', 'confirm_password','profile_pic']
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match")
    #     return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username','email','password']