from django import forms
from .models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'roll_number', 'departmet']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Roll Number'}),
            'departmet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department'}),
        }
