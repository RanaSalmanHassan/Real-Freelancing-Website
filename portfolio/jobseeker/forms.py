from django import forms
from .models import Apply_Job

class Apply_Job_Form(forms.ModelForm):
    class Meta:
        model = Apply_Job
        exclude = ('applier','job_applied')