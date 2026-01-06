from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['roll_no', 'student_class', 'department']

        # Bootstrap styling ke liye
        widgets = {
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Roll Number'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
