# Generated by Django 4.1.1 on 2023-03-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_remove_create_job_required_skills_and_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_job',
            name='relevent_files',
            field=models.FileField(blank=True, null=True, upload_to='admin/relevent_files'),
        ),
    ]
