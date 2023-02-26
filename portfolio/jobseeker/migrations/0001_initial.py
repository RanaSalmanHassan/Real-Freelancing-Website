# Generated by Django 4.1.1 on 2023-02-26 05:27

from django.db import migrations, models
import jobseeker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=7)),
                ('passport_country', models.CharField(choices=[('Australia', 'Australia'), ('Brazil', 'Brazil'), ('Canada', 'Canada'), ('China', 'China'), ('France', 'France'), ('Germany', 'Germany'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Mexico', 'Mexico'), ('Netherlands', 'Netherlands'), ('Nigeria', 'Nigeria'), ('Pakistan', 'Pakistan'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Russia', 'Russia'), ('Saudi Arabia', 'Saudi Arabia'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Algeria', 'Algeria'), ('Argentina', 'Argentina'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Colombia', 'Colombia'), ('Egypt', 'Egypt'), ('Iraq', 'Iraq'), ('Kazakhstan', 'Kazakhstan'), ('Malaysia', 'Malaysia'), ('Morocco', 'Morocco'), ('Myanmar', 'Myanmar'), ('Peru', 'Peru'), ('Romania', 'Romania'), ('South Sudan', 'South Sudan'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Other', 'Other')], default='Select', max_length=25)),
                ('current_location', models.CharField(choices=[('Australia', 'Australia'), ('Brazil', 'Brazil'), ('Canada', 'Canada'), ('China', 'China'), ('France', 'France'), ('Germany', 'Germany'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Mexico', 'Mexico'), ('Netherlands', 'Netherlands'), ('Nigeria', 'Nigeria'), ('Pakistan', 'Pakistan'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Russia', 'Russia'), ('Saudi Arabia', 'Saudi Arabia'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Algeria', 'Algeria'), ('Argentina', 'Argentina'), ('Bangladesh', 'Bangladesh'), ('Belgium', 'Belgium'), ('Colombia', 'Colombia'), ('Egypt', 'Egypt'), ('Iraq', 'Iraq'), ('Kazakhstan', 'Kazakhstan'), ('Malaysia', 'Malaysia'), ('Morocco', 'Morocco'), ('Myanmar', 'Myanmar'), ('Peru', 'Peru'), ('Romania', 'Romania'), ('South Sudan', 'South Sudan'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('Uzbekistan', 'Uzbekistan'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Other', 'Other')], default='Select', max_length=25)),
                ('name_of_city_currently_based', models.CharField(blank=True, max_length=25)),
                ('level_of_english_language', models.CharField(choices=[('Native', 'Native'), ('Fluent', 'Fluent'), ('Working Knowledge', 'Working Knowledge')], default='Fluent', max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Career_Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_place', models.CharField(blank=True, max_length=40)),
                ('second_place', models.CharField(blank=True, max_length=40)),
                ('third_place', models.CharField(blank=True, max_length=40)),
                ('min_expected_salary_amount', models.CharField(blank=True, max_length=40)),
                ('min_expected_salary_currency', models.CharField(blank=True, choices=[('per month', 'per month'), ('per year', 'per year')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counrty_code', models.CharField(choices=[('Australia', '+61'), ('Brazil', '+55'), ('Canada', '+1'), ('China', '+86'), ('France', '+33'), ('Germany', '+49'), ('India', '+91'), ('Indonesia', '+62'), ('Iran', '+98'), ('Italy', '+39'), ('Japan', '+81'), ('Mexico', '+52'), ('Netherlands', '+31'), ('Nigeria', '+234'), ('Pakistan', '+92'), ('Philippines', '+63'), ('Poland', '+48'), ('Russia', '+7'), ('Saudi Arabia', '+966'), ('South Africa', '+27'), ('South Korea', '+82'), ('Spain', '+34'), ('Sweden', '+46'), ('Switzerland', '+41'), ('Taiwan', '+886'), ('Thailand', '+66'), ('Turkey', '+90'), ('Ukraine', '+380'), ('United Arab Emirates', '+971'), ('United Kingdom', '+44'), ('United States', '+1'), ('Algeria', '+213'), ('Argentina', '+54'), ('Bangladesh', '+880'), ('Belgium', '+32'), ('Colombia', '+57'), ('Egypt', '+20'), ('Iraq', '+964'), ('Kazakhstan', '+7'), ('Malaysia', '+60'), ('Morocco', '+212'), ('Myanmar', '+95'), ('Peru', '+51'), ('Romania', '+40'), ('South Sudan', '+211'), ('Tanzania', '+255'), ('Uganda', '+256'), ('Uzbekistan', '+998'), ('Venezuela', '+58'), ('Vietnam', '+84')], default='Select', max_length=20)),
                ('area_code', models.CharField(default='Select', max_length=10, validators=[jobseeker.models.only_integer])),
                ('actual_number', models.CharField(max_length=10, validators=[jobseeker.models.only_integer])),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Work', 'Work'), ('Mobile', 'Mobile'), ('Other', 'Other')], default='Other', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Current_Employement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_of_company', models.CharField(blank=True, max_length=40)),
                ('current_position', models.CharField(blank=True, max_length=40)),
                ('job_category', models.CharField(blank=True, max_length=40)),
                ('experience', models.CharField(blank=True, max_length=40)),
                ('name_of_company', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.BooleanField(default=True)),
                ('fresh_graduate_or_university_student', models.BooleanField(default=False)),
                ('subject_in_university', models.CharField(choices=[('Accounting', 'Accounting'), ('Art History', 'Art History'), ('Biology', 'Biology'), ('Business Administration', 'Business Administration'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Economics', 'Economics'), ('Education', 'Education'), ('Electrical Engineering', 'Electrical Engineering'), ('English Literature', 'English Literature'), ('Environmental Science', 'Environmental Science'), ('Finance', 'Finance'), ('Graphic Design', 'Graphic Design'), ('History', 'History'), ('International Relations', 'International Relations'), ('Journalism', 'Journalism'), ('Marketing', 'Marketing'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Music', 'Music'), ('Nursing', 'Nursing'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Sociology', 'Sociology'), ('Statistics', 'Statistics'), ('Theater', 'Theater'), ('Visual Arts', 'Visual Arts'), ('Other/No University', 'Other/No University')], default='Select', max_length=100)),
            ],
        ),
    ]