from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Department, Position


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['position', 'departament', 'profile_picture']

class PositionsUpdateForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position']

class DepartmentsUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department']

