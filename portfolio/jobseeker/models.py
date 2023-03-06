from django.db import models
from loginapp.models import User
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

from employer.models import Create_Job
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
Country_Choices = (('Australia', 'Australia'),
                   ('Brazil', 'Brazil'),
                   ('Canada', 'Canada'),
                   ('China', 'China'),
                   ('France', 'France'),
                   ('Germany', 'Germany'),
                   ('India', 'India'),
                   ('Indonesia', 'Indonesia'),
                   ('Iran', 'Iran'),
                   ('Italy', 'Italy'),
                   ('Japan', 'Japan'),
                   ('Mexico', 'Mexico'),
                   ('Netherlands', 'Netherlands'),
                   ('Nigeria', 'Nigeria'),
                   ('Pakistan', 'Pakistan'),
                   ('Philippines', 'Philippines'),
                   ('Poland', 'Poland'),
                   ('Russia', 'Russia'),
                   ('Saudi Arabia', 'Saudi Arabia'),
                   ('South Africa', 'South Africa'),
                   ('South Korea', 'South Korea'),
                   ('Spain', 'Spain'),
                   ('Sweden', 'Sweden'),
                   ('Switzerland', 'Switzerland'),
                   ('Taiwan', 'Taiwan'),
                   ('Thailand', 'Thailand'),
                   ('Turkey', 'Turkey'),
                   ('Ukraine', 'Ukraine'),
                   ('United Arab Emirates', 'United Arab Emirates'),
                   ('United Kingdom', 'United Kingdom'),
                   ('United States', 'United States'),
                   ('Algeria', 'Algeria'),
                   ('Argentina', 'Argentina'),
                   ('Bangladesh', 'Bangladesh'),
                   ('Belgium', 'Belgium'),
                   ('Colombia', 'Colombia'),
                   ('Egypt', 'Egypt'),
                   ('Iraq', 'Iraq'),
                   ('Kazakhstan', 'Kazakhstan'),
                   ('Malaysia', 'Malaysia'),
                   ('Morocco', 'Morocco'),
                   ('Myanmar', 'Myanmar'),
                   ('Peru', 'Peru'),
                   ('Romania', 'Romania'),
                   ('South Sudan', 'South Sudan'),
                   ('Tanzania', 'Tanzania'),
                   ('Uganda', 'Uganda'),
                   ('Uzbekistan', 'Uzbekistan'),
                   ('Venezuela', 'Venezuela'),
                   ('Vietnam', 'Vietnam'),
                   ('Other', 'Other')
                   )
language_choices = (
    ('Native', 'Native'),
    ('Fluent', 'Fluent'),
    ('Working Knowledge', 'Working Knowledge')
)

Country_Wise_Phone_Number_Codes = (('Australia', '+61'),
                                   ('Brazil', '+55'),
                                   ('Canada', '+1'),
                                   ('China', '+86'),
                                   ('France', '+33'),
                                   ('Germany', '+49'),
                                   ('India', '+91'),
                                   ('Indonesia', '+62'),
                                   ('Iran', '+98'),
                                   ('Italy', '+39'),
                                   ('Japan', '+81'),
                                   ('Mexico', '+52'),
                                   ('Netherlands', '+31'),
                                   ('Nigeria', '+234'),
                                   ('Pakistan', '+92'),
                                   ('Philippines', '+63'),
                                   ('Poland', '+48'),
                                   ('Russia', '+7'),
                                   ('Saudi Arabia', '+966'),
                                   ('South Africa', '+27'),
                                   ('South Korea', '+82'),
                                   ('Spain', '+34'),
                                   ('Sweden', '+46'),
                                   ('Switzerland', '+41'),
                                   ('Taiwan', '+886'),
                                   ('Thailand', '+66'),
                                   ('Turkey', '+90'),
                                   ('Ukraine', '+380'),
                                   ('United Arab Emirates', '+971'),
                                   ('United Kingdom', '+44'),
                                   ('United States', '+1'),
                                   ('Algeria', '+213'),
                                   ('Argentina', '+54'),
                                   ('Bangladesh', '+880'),
                                   ('Belgium', '+32'),
                                   ('Colombia', '+57'),
                                   ('Egypt', '+20'),
                                   ('Iraq', '+964'),
                                   ('Kazakhstan', '+7'),
                                   ('Malaysia', '+60'),
                                   ('Morocco', '+212'),
                                   ('Myanmar', '+95'),
                                   ('Peru', '+51'),
                                   ('Romania', '+40'),
                                   ('South Sudan', '+211'),
                                   ('Tanzania', '+255'),
                                   ('Uganda', '+256'),
                                   ('Uzbekistan', '+998'),
                                   ('Venezuela', '+58'),
                                   ('Vietnam', '+84'))
type_of_phone_number = (
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Mobile', 'Mobile'),
    ('Other', 'Other'),
)

Undergraduate_Subject_Choices = (('Accounting', 'Accounting'),
                                 ('Art History', 'Art History'),
                                 ('Biology', 'Biology'),
                                 ('Business Administration',
                                  'Business Administration'),
                                 ('Chemistry', 'Chemistry'),
                                 ('Civil Engineering', 'Civil Engineering'),
                                 ('Computer Science', 'Computer Science'),
                                 ('Economics', 'Economics'),
                                 ('Education', 'Education'),
                                 ('Electrical Engineering',
                                  'Electrical Engineering'),
                                 ('English Literature', 'English Literature'),
                                 ('Environmental Science',
                                  'Environmental Science'),
                                 ('Finance', 'Finance'),
                                 ('Graphic Design', 'Graphic Design'),
                                 ('History', 'History'),
                                 ('International Relations',
                                  'International Relations'),
                                 ('Journalism', 'Journalism'),
                                 ('Marketing', 'Marketing'),
                                 ('Mathematics', 'Mathematics'),
                                 ('Mechanical Engineering',
                                  'Mechanical Engineering'),
                                 ('Music', 'Music'),
                                 ('Nursing', 'Nursing'),
                                 ('Philosophy', 'Philosophy'),
                                 ('Physics', 'Physics'),
                                 ('Political Science', 'Political Science'),
                                 ('Psychology', 'Psychology'),
                                 ('Sociology', 'Sociology'),
                                 ('Statistics', 'Statistics'),
                                 ('Theater', 'Theater'),
                                 ('Visual Arts', 'Visual Arts'),
                                 ('Other/No University', 'Other/No University'))
month_year_choice = (
    ('per month', 'per month'),
    ('per year', 'per year'),

)

currency_choices = (
    ('US Dollar', 'US Dollar'),
    ('Euro', 'Euro'),
    ('Japanese Yen', 'Japanese Yen'),
    ('British Pound Sterling', 'British Pound Sterling'),
    ('Australian Dollar', 'Australian Dollar'),
    ('Canadian Dollar', 'Canadian Dollar'),
    ('Swiss Franc', 'Swiss Franc'),
    ('Chinese Yuan', 'Chinese Yuan'),
    ('Hong Kong Dollar', 'Hong Kong Dollar'),
    ('New Zealand Dollar', 'New Zealand Dollar'),
    ('South Korean Won', 'South Korean Won'),
    ('Singapore Dollar', 'Singapore Dollar'),
    ('Swedish Krona', 'Swedish Krona'),
    ('Norwegian Krone', 'Norwegian Krone'),
    ('Mexican Peso', 'Mexican Peso'),
    ('Indian Rupee', 'Indian Rupee'),
    ('Russian Ruble', 'Russian Ruble'),
    ('South African Rand', 'South African Rand'),
    ('Brazilian Real', 'Brazilian Real'),
    ('Turkish Lira', 'Turkish Lira'),
    ('Polish Zloty', 'Polish Zloty'),
    ('Danish Krone', 'Danish Krone'),
    ('Thai Baht', 'Thai Baht'),
    ('UAE Dirham', 'UAE Dirham'),
    ('Pakistani Rupee', 'Pakistani Rupee')
)
def only_integer(value):
    if value.isdigit() == False:
        raise ValidationError('Contact Number should only contain numbers!')


class Basic_Info(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField (
        User, on_delete=models.SET_NULL, related_name='user_basic_info', null=True)
    profile_pic = models.ImageField(upload_to='user_pics',default='user.png')
    first_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)

    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=gender_choices,
                              default='Male', max_length=7,blank=True,null=True)
    passport_country = models.CharField(
        default='Select', choices=Country_Choices, max_length=25,blank=True,null=True)
    current_location = models.CharField(
        default='Select', choices=Country_Choices, max_length=25,blank=True,null=True)
    name_of_city_currently_based = models.CharField( max_length=25,blank=True,null=True)
    level_of_english_language = models.CharField(
        choices=language_choices, default='Fluent', max_length=17,blank=True,null=True)


class Contact_Details(models.Model):
    user = models.OneToOneField (
        User, on_delete=models.SET_NULL, related_name='user_contact_info', null=True)
    counrty_code = models.CharField(max_length=20,
                                    choices=Country_Wise_Phone_Number_Codes, default='Select',blank=True,null=True)
    area_code = models.CharField(
        validators=[only_integer], max_length=10, default='Select',blank=True,null=True)
    actual_number = models.CharField(validators=[only_integer], max_length=10,blank=True,null=True)
    type = models.CharField(choices=type_of_phone_number,
                            default='Other', max_length=50,blank=True,null=True)


class Education(models.Model):
    user = models.OneToOneField (
        User, on_delete=models.SET_NULL, related_name='user_education', null=True)
    degree = models.BooleanField(default=True)
    fresh_graduate_or_university_student = models.BooleanField(default=False)
    subject_in_university = models.CharField(max_length=100,
                                             choices=Undergraduate_Subject_Choices, default='Select',blank=True,null=True)


class Current_Employement(models.Model):
    user = models.OneToOneField (
        User, on_delete=models.SET_NULL, related_name='user_employement', null=True)
    name_of_company = models.CharField(max_length=40, blank=True,null=True)
    activity_of_company = models.CharField(max_length=40, blank=True,null=True)
    current_position = models.CharField(max_length=40, blank=True,null=True)
    job_category = models.CharField(max_length=40, blank=True,null=True)
    experience = models.CharField(max_length=40, blank=True,null=True)


class Career_Preference(models.Model):
    user = models.OneToOneField (
        User, on_delete=models.SET_NULL, related_name='user_pref', null=True)
    first_place = models.CharField(max_length=40, blank=True,null=True)
    second_place = models.CharField(max_length=40, blank=True,null=True)
    third_place = models.CharField(max_length=40, blank=True,null=True)
    min_expected_salary_amount = models.CharField(max_length=40, blank=True)
    min_expected_salary_currency = models.CharField(max_length=40,
                                                    blank=True, choices=currency_choices,null=True)
    monthly_yearly_choice = models.CharField(max_length=40,
                                                    blank=True, choices=month_year_choice,null=True)
    

@receiver(post_save, sender=User)
def create_or_save_profile(sender, instance, created, **kwargs):
    if created and instance.is_job_seeker:
        Basic_Info.objects.create(user=instance)
        Education.objects.create(user=instance)
        Contact_Details.objects.create(user=instance)
        Current_Employement.objects.create(user=instance)
        Career_Preference.objects.create(user=instance)
    elif not created and instance.is_job_seeker:
        instance.user_basic_info.save()
        instance.user_education.save()
        instance.user_contact_info.save()
        instance.user_employement.save()
        instance.user_pref.save()


class Apply_Job(models.Model):
    applier = models.ForeignKey(User,on_delete=models.CASCADE,related_name='job_applier')
    job_applied = models.ForeignKey(Create_Job,on_delete=models.SET_NULL,related_name='job_appled',null=True)
    cover_letter = models.TextField()
    cv = models.FileField(blank=False,null=False)