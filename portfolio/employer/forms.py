from django import forms
from .models import Create_Job


class Create_Job_Form(forms.ModelForm):
    class Meta:
        model = Create_Job
        exclude = ('admin',)
