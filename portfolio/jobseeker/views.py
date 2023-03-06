from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Basic_Info, Education, Contact_Details, Current_Employement, Career_Preference
from django.contrib import messages
from employer.models import Create_Job
from .forms import Apply_Job_Form
# Create your views here.


@login_required(login_url='loginapp:login')
def basic_info(request):
    try:
        basic_info = Basic_Info.objects.get(user=request.user)
    except Basic_Info.DoesNotExist:
        basic_info = None

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
            if basic_info:
                basic_info.first_name = first_name
                basic_info.last_name = last_name
                basic_info.date_of_birth = date_of_birth
                basic_info.gender = gender
                basic_info.passport_country = country_pp
                basic_info.current_location = country_loc
                basic_info.name_of_city_currently_based = city_name
                basic_info.level_of_english_language = english_level
            else:
                basic_info = Basic_Info.objects.create(
                    user=request.user, first_name=first_name, last_name=last_name,
                    date_of_birth=date_of_birth, gender=gender, passport_country=country_pp,
                    current_location=country_loc, name_of_city_currently_based=city_name,
                    level_of_english_language=english_level
                )

            basic_info.save()
            messages.success(request, 'Basic information saved!')
            return HttpResponseRedirect(reverse('jobseeker:profile/education'))

        else:
            messages.error(request, 'Please Fill all fields!')
            return HttpResponseRedirect(reverse('jobseeker:profile/basic_info'))

    else:
        return render(request, 'jobseeker/profile/basic_info.html', {'basic_info': basic_info})



@login_required(login_url='loginapp:login')
def education(request):
    try:
        education_det = Education.objects.get(user=request.user)
    except Education.DoesNotExist:
        education_det = None

    if request.method == 'POST':
        degree = request.POST.get('degree', None)
        fresh_university = request.POST.get('fresh_university', None)
        undergrad_subject = request.POST.get('undergrad_subject', None)

        required_fields = ['degree', 'fresh_university', 'undergrad_subject']
        if all(field in request.POST for field in required_fields):
            if education_det:
                education_det.degree = degree
                education_det.fresh_graduate_or_university_student = fresh_university
                education_det.subject_in_university = undergrad_subject
            else:
                education_det = Education.objects.create(
                    user=request.user,
                    degree=degree,
                    fresh_graduate_or_university_student=fresh_university,
                    subject_in_university=undergrad_subject
                )

            education_det.save()
            messages.success(request, 'Education details saved!')
            return HttpResponseRedirect(reverse('jobseeker:profile'))

        else:
            messages.error(request, 'Please fill in all required fields.')
            return HttpResponseRedirect(reverse('jobseeker:profile/education'))

    else:
        return render(request, 'jobseeker/profile/education.html', {'education_det': education_det})



@login_required(login_url='loginapp:login')
def contact_det(request):
    try:
        contact_details = Contact_Details.objects.get(user=request.user)
    except Contact_Details.DoesNotExist:
        contact_details = None

    if request.method == 'POST':
        country_code = request.POST.get('country_code', None)
        area_code = request.POST.get('area_code', None)
        phone_number = request.POST.get('phone_number', None)
        phone_type = request.POST.get('phone_type', None)

        if contact_details:
            contact_details.counrty_code = country_code
            contact_details.area_code = area_code
            contact_details.actual_number = phone_number
            contact_details.type = phone_type
        else:
            contact_details = Contact_Details.objects.create(
                user=request.user, counrty_code=country_code,
                area_code=area_code, actual_number=phone_number, type=phone_type
            )

        contact_details.save()
        messages.success(request, 'Contact details saved!')
        return HttpResponseRedirect(reverse('jobseeker:profile'))
    else:
        return render(request, 'jobseeker/profile/contact_det.html', {'contact_details': contact_details})



@login_required(login_url='loginapp:login')
def current_emp(request):
    try:
        current_emp = Current_Employement.objects.get(user=request.user)
    except Current_Employement.DoesNotExist:
        current_emp = None

    if request.method == 'POST':
        comp_name = request.POST.get('comp_name', None)
        comp_act = request.POST.get('comp_act', None)
        user_pos = request.POST.get('user_pos', None)
        user_cat = request.POST.get('user_cat', None)
        user_exp = request.POST.get('user_exp', None)

        if current_emp:
            current_emp.name_of_company = comp_name
            current_emp.activity_of_company = comp_act
            current_emp.current_position = user_pos
            current_emp.job_category = user_cat
            current_emp.experience = user_exp
        else:
            current_emp = Current_Employement.objects.create(
                user=request.user,
                name_of_company=comp_name,
                activity_of_company=comp_act,
                current_position=user_pos,
                job_category=user_cat,
                experience=user_exp,
            )

        current_emp.save()
        messages.success(request, 'Current Employment saved!')
        return HttpResponseRedirect(reverse('jobseeker:profile/career_pref'))

    else:
        return render(request, 'jobseeker/profile/curr_employment.html', {'current_emp': current_emp})




@login_required(login_url='loginapp:login')
def career_pref(request):
    try:
        career_pref = Career_Preference.objects.get(user=request.user)
    except Career_Preference.DoesNotExist:
        career_pref = None

    if request.method == 'POST':
        first_pre_loc = request.POST.get('first_pre_loc', None)
        second_pre_loc = request.POST.get('second_pre_loc', None)
        third_pre_loc = request.POST.get('third_pre_loc', None)
        min_amount = request.POST.get('min_amount', None)
        currency = request.POST.get('currency', None)
        frequency = request.POST.get('frequency', None)

        if career_pref:
            career_pref.first_place = first_pre_loc
            career_pref.second_place = second_pre_loc
            career_pref.third_place = third_pre_loc
            career_pref.min_expected_salary_amount = min_amount
            career_pref.min_expected_salary_currency = currency
            career_pref.monthly_yearly_choice = frequency
        else:
            career_pref = Career_Preference.objects.create(
                user=request.user, first_place=first_pre_loc, second_place=second_pre_loc,
                third_place=third_pre_loc, min_expected_salary_amount=min_amount,
                min_expected_salary_currency=currency, monthly_yearly_choice=frequency
            )

        career_pref.save()
        messages.success(request, 'Career preference saved!')
        return HttpResponseRedirect(reverse('jobseeker:profile'))
    else:
        return render(request, 'jobseeker/profile/career_pref.html', {'career_pref': career_pref})


@login_required(login_url='loginapp:login')
def profile(request):
    return render(request,'jobseeker/profile/profile.html')


def search(request):
    searched_query = request.GET.get('search_jobs', None)
    if searched_query:
        searched_results = Create_Job.objects.filter(job_title__icontains=searched_query)
    else:
        searched_results = None
    context = {'searched_results': searched_results,'searched_query':searched_query}
    return render(request, 'jobseeker/search.html', context)

@login_required(login_url='loginapp:login')
def apply_for_job(request,pk):
    job_applied = Create_Job.objects.get(pk=pk)
    current_user = request.user
    if current_user.is_job_seeker:
        form = Apply_Job_Form()
        if request.method == 'POST':
            form = Apply_Job_Form(request.POST,request.FILES)
            if form.is_valid():
                if current_user.user_basic_info and current_user.user_contact_info and current_user.user_education and current_user.user_employement and current_user.user_pref:


                    form_instance = form.save(commit=False)
                    form_instance.applier = request.user
                    form_instance.job_applied = job_applied
                    form_instance.save()
                    messages.success(request,'Successfully Applied for Job!')
                    return HttpResponseRedirect(reverse('index'))
                else:
                    messages.warning(request,'Please Complete Profile Before Applying!')
                    return HttpResponseRedirect(reverse('loginapp:profile'))
                
            else:
                print(form.errors)
                messages.error(request,'Please Fill The Form Correctly!')
                return HttpResponseRedirect(reverse('jobseeker:apply_for_jobs'))
        dict = {'form':form,'job_applied':job_applied}
        return render(request,'jobseeker/apply_for_jobs.html',dict)
    else:
        messages.warning(request,'You Can`t Access This Page!')
        return HttpResponseRedirect(reverse('loginapp:login'))


