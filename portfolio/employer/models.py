from django.db import models
from loginapp.models import User
# Create your models here.

job_categories = (
    ('Data Scientist', 'Data Scientist'),
    ('Software Engineer', 'Software Engineer'),
    ('Product Manager', 'Product Manager'),
    ('UX Designer', 'UX Designer'),
    ('Marketing Manager', 'Marketing Manager'),
    ('Business Analyst', 'Business Analyst'),
    ('Financial Analyst', 'Financial Analyst'),
    ('Account Manager', 'Account Manager'),
    ('Sales Manager', 'Sales Manager'),
    ('Customer Service Representative', 'Customer Service Representative'),
    ('Human Resources Manager', 'Human Resources Manager'),
    ('Operations Manager', 'Operations Manager'),
    ('Project Manager', 'Project Manager'),
    ('Quality Assurance Engineer', 'Quality Assurance Engineer'),
    ('Graphic Designer', 'Graphic Designer'),
    ('Web Developer', 'Web Developer'),
    ('Mobile Developer', 'Mobile Developer'),
    ('UI Designer', 'UI Designer'),
    ('IT Manager', 'IT Manager'),
    ('Network Administrator', 'Network Administrator'),
    ('Database Administrator', 'Database Administrator'),
    ('DevOps Engineer', 'DevOps Engineer'),
    ('Cloud Architect', 'Cloud Architect'),
    ('Cybersecurity Analyst', 'Cybersecurity Analyst'),
    ('Artificial Intelligence Engineer', 'Artificial Intelligence Engineer'),
    ('Machine Learning Engineer', 'Machine Learning Engineer'),
    ('Data Analyst', 'Data Analyst'),
    ('Product Designer', 'Product Designer'),
    ('Content Writer', 'Content Writer'),
    ('Social Media Manager', 'Social Media Manager'),
    ('Brand Manager', 'Brand Manager'),
    ('Public Relations Manager', 'Public Relations Manager'),
    ('Event Coordinator', 'Event Coordinator'),
    ('Logistics Coordinator', 'Logistics Coordinator'),
    ('Supply Chain Manager', 'Supply Chain Manager'),
    ('Procurement Specialist', 'Procurement Specialist'),
    ('Financial Advisor', 'Financial Advisor'),
    ('Investment Banker', 'Investment Banker'),
    ('Management Consultant', 'Management Consultant'),
    ('Executive Assistant', 'Executive Assistant'),
    ('Personal Assistant', 'Personal Assistant'),
    ('Travel Agent', 'Travel Agent'),
    ('Hotel Manager', 'Hotel Manager'),
    ('Restaurant Manager', 'Restaurant Manager'),
    ('Chef', 'Chef'),
    ('Baker', 'Baker'),
    ('Pastry Chef', 'Pastry Chef'),
    ('Nurse', 'Nurse'),
    ('Physician', 'Physician'),
    ('Surgeon', 'Surgeon'),
    ('Pharmacist', 'Pharmacist'),
    ('Dentist', 'Dentist'),
    ('Physical Therapist', 'Physical Therapist'),
    ('Occupational Therapist', 'Occupational Therapist'),
    ('Speech Therapist', 'Speech Therapist'),
    ('Clinical Psychologist', 'Clinical Psychologist'),
    ('Social Worker', 'Social Worker'),
    ('Teacher', 'Teacher'),
    ('Professor', 'Professor'),
    ('Librarian', 'Librarian'),
    ('Architect', 'Architect'),
    ('Civil Engineer', 'Civil Engineer'),
    ('Mechanical Engineer', 'Mechanical Engineer'),
    ('Electrical Engineer', 'Electrical Engineer'),
    ('Chemical Engineer', 'Chemical Engineer'),
    ('Aerospace Engineer', 'Aerospace Engineer'),
    ('Environmental Scientist', 'Environmental Scientist'),
    ('Geologist', 'Geologist'),
    ('Marine Biologist', 'Marine Biologist'),
    ('Zoologist', 'Zoologist'),
    ('Journalist', 'Journalist'),
    ('Photographer', 'Photographer'),
)
class Create_Job(models.Model):
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin_job')
    job_title = models.CharField(max_length=30,blank=False,null=False)
    job_description = models.TextField(blank=False,null=False)
    budget = models.CharField(max_length=30,blank=False,null=False)
    payment_terms = models.CharField(max_length=40,blank=False,null=False)
    categories = models.CharField(choices=job_categories,max_length=32,blank=False,null=False)
    relevent_files = models.FileField(upload_to='admin/relevent_files',blank=True,null=True)

    def __str__(self):
        return (f'{self.job_title} in {self.categories}')