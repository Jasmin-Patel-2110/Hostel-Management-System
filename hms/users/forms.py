from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Student

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass


class OnboardingForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'enrollment_number', 'name', 'gender', 'branch', 'semester',
            'contact_number', 'parent_contact_number', 'email', 'status'
        ]
        widgets = {
            'enrollment_number': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Enrollment Number',
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Full Name',
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
            }),
            'branch': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
            }),
            'semester': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Contact Number',
            }),
            'parent_contact_number': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Parent\'s Contact Number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
                'placeholder': 'Email Address',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded',
            }),
        }