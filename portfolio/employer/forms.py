from django import forms
from .models import Create_Job


class Create_Job_Form(forms.ModelForm):
    class Meta:
        model = Create_Job
        exclude = ('admin',)
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'job_title'}),
            'job_description': forms.Textarea(attrs={'class': 'job_description'}),
            'budget': forms.TextInput(attrs={'class': 'budget'}),
            'payment_terms': forms.TextInput(attrs={'class': 'payment_terms'}),
            'required_skills_and_qualification': forms.TextInput(attrs={'class': 'required_skills_and_qualification'}),
            'relevent_files': forms.TextInput(attrs={'class': 'relevent_files'}),
        }
