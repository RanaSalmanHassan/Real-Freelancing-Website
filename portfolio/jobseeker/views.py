from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Basic_Info, Education, Contact_Details, Current_Employement, Career_Preference
from django.contrib import messages
# Create your views here.


@login_required(login_url='loginapp:login')
def basic_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        date_of_birth = request.POST.get('date_of_birth', None)
        gender = request.POST.get('gender', None)
        country_pp = request.POST.get('country_pp', None)
        country_loc = request.POST.get('country_loc', None)
        city_name = request.POST.get('city_name', None)
        english_level = request.POST.get('english_level', None)

        required_fields = ['first_name', 'last_name', 'date_of_birth',
                           'gender', 'country_pp', 'country_loc', 'city_name', 'english_level']
        if all(field in request.POST for field in required_fields):

            Basic_Info.objects.create(user=request.user, first_name=first_name, last_name=last_name,
                                      date_of_birth=date_of_birth, gender=gender, passport_country=country_pp, current_location=country_loc, name_of_city_currently_based=city_name, level_of_english_language=english_level)
            return HttpResponseRedirect(reverse('jobseeker:profile/education'))

        else:
            messages.error(request, 'Please Fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/basic_info'))

    else:
        return render(request, 'jobseeker/profile/basic_info.html')


@login_required(login_url='loginapp:login')
def education(request):
    if request.method == 'POST':
        degree = request.POST.get('degree', None)
        degree = bool(degree)
        fresh_university = request.POST.get('fresh_university', None)
        fresh_university = bool(fresh_university)
        undergrad_subject = request.POST.get('undergrad_subject', None)

        required_fields = ['degree', 'fresh_university', 'undergrad_subject']
        if all(field in request.POST for field in required_fields):

            Education.objects.create(user=request.user, degree=degree,
                                     fresh_graduate_or_university_student=fresh_university, subject_in_university=undergrad_subject)
            return HttpResponseRedirect(reverse('jobseeker:profile/contact_det'))

        else:
            messages.error(request, 'Please Fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/education'))

    else:
        return render(request, 'jobseeker/profile/education.html')


@login_required(login_url='loginapp:login')
def contact_det(request):

    if request.method == 'POST':
        phone_code1 = request.POST.get('phone_code1', None)
        area_code1 = request.POST.get('area_code1', None)
        phone_number1 = request.POST.get('phone_number1', None)
        phone_type1 = request.POST.get('phone_type1', None)

        required_fields = ['phone_code1', 'area_code1',
                           'phone_number1', 'phone_type1']
        if all(field in request.POST for field in required_fields):

            Contact_Details.objects.create(user=request.user, counrty_code=phone_code1,
                                           area_code=area_code1, actual_number=phone_number1, type=phone_type1)
            return HttpResponseRedirect(reverse('jobseeker:profile/current_emp'))

        else:
            messages.error(request, 'Please Fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/contact_det'))

    else:
        return render(request, 'jobseeker/profile/contact_det.html')


@login_required(login_url='loginapp:login')
def current_emp(request):

    if request.method == 'POST':
        comp_name = request.POST.get('comp_name', None)
        comp_act = request.POST.get('comp_act', None)
        user_pos = request.POST.get('user_pos', None)
        user_cat = request.POST.get('user_cat', None)
        user_exp = request.POST.get('user_exp', None)

        required_fields = ['comp_name', 'comp_act',
                           'user_pos', 'user_cat', 'user_exp']
        if all(field in request.POST for field in required_fields):

            Current_Employement.objects.create(user=request.user, name_of_company=comp_name, activity_of_company=comp_act,
                                               current_position=user_pos, job_category=user_cat, experience=user_exp)
            return HttpResponseRedirect(reverse('jobseeker:profile/career_pref'))

        else:
            messages.error(request, 'Please Fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/current_emp'))

    else:
        return render(request, 'jobseeker/profile/curr_employment.html')


@login_required(login_url='loginapp:login')
def career_pref(request):
    if request.method == 'POST':
        first_pre_loc = request.POST.get('first_pre_loc', None)
        second_pre_loc = request.POST.get('second_pre_loc', None)
        third_pre_loc = request.POST.get('third_pre_loc', None)
        min_amount = request.POST.get('min_amount', None)
        currency = request.POST.get('currency', None)
        frequency = request.POST.get('frequency', None)

        required_fields = ['first_pre_loc',
                           'min_amount', 'currency', 'frequency']
        if all(field in request.POST for field in required_fields):
            Career_Preference.objects.create(
                user=request.user, first_place=first_pre_loc, second_place=second_pre_loc,
                third_place=third_pre_loc, min_expected_salary_amount=min_amount,
                min_expected_salary_currency=currency, monthly_yearly_choice=frequency
            )
            return HttpResponse('Thanks XD!')
        else:
            messages.error(request, 'Please fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/career_pref'))
    else:
        return render(request, 'jobseeker/profile/career_pref.html')
