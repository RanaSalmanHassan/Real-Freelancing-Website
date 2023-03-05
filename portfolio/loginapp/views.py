from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SignUpForm, LoginForm
# Create your views here.
from django.contrib import messages
from .models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_job_seeker = True
            user.save()
            return HttpResponseRedirect(reverse('loginapp:login'))
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user_var = authenticate(username=username, password=password)
            # if user_var is not None and user_var.is_job_seeker:
            #     login(request, user_var)
            #     messages.success(request,'Signed Up Successfully!')
            #     messages.info(request,'Remember! You can`t apply for Jobs untill You complete Your Profile!')
            #     return HttpResponseRedirect(reverse('jobseeker:profile'))


            # elif user_var is not None and user_var.is_admin:
            #     login(request,user_var)
            #     messages.success(request,'Signed Up Admin Successfully!')
            #     return HttpResponseRedirect(reverse('employer:create_job_view'))
            # else:
            #     return HttpResponse('Go away')
        else:
            # Print out the form errors to the console
            print(form.errors)
            # Add an error message to the messages framework
            messages.error(
                request, f'There was an error with your submission => {form.errors}')
    else:
        form = SignUpForm()

    return render(request, 'loginapp/signup.html', {'form': form})

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_job_seeker:
                login(request, user)

                messages.success(request,'Logged In Successfully!')
                messages.info(request,'Remember You can`t apply for jobs untill you have completed your profile')
                return HttpResponseRedirect(reverse('jobseeker:profile'))
            elif user is not None and user.is_admin:
                login(request,user)
                messages.success(request,'Signed Up Admin Successfully!')
                return HttpResponseRedirect(reverse('employer:create_job_view'))
            else:
                return HttpResponse('Go away')
        else:
            # Print out the form errors to the console
            print(form.errors)
            # Add an error message to the messages framework
            messages.error(
                request, f'There was an error with your submission : {form.errors} Please try again.')

    dict = {'form': form}
    return render(request, 'loginapp/login.html', dict)

def logout_view(request):
    logout(request)
    messages.warning(request,'You are Logged Out!')
    return HttpResponseRedirect(reverse('loginapp:login'))