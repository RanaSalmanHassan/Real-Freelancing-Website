# Generated by Django 4.1.1 on 2023-03-03 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('budget', models.CharField(max_length=30)),
                ('payment_terms', models.CharField(max_length=40)),
                ('required_skills_and_qualification', models.CharField(max_length=300)),
                ('relevent_files', models.FileField(upload_to='admin/relevent_files')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_job', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
