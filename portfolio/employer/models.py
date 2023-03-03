from django.db import models
from loginapp.models import User
# Create your models here.


class Create_Job(models.Model):
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin_job')
    job_title = models.CharField(max_length=30)
    job_description = models.TextField()
    budget = models.CharField(max_length=30)
    payment_terms = models.CharField(max_length=40)
    required_skills_and_qualification = models.CharField(max_length=300)
    relevent_files = models.FileField(upload_to='admin/relevent_files')
