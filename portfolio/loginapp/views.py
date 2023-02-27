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
            messages.success(request, 'ACCOUNT CREATED SUCCESSFULLY!')
            return HttpResponse('SIGN UP SUCCESSFUL')
        else:
            # Print out the form errors to the console
            print(form.errors)
            # Add an error message to the messages framework
            messages.error(
                request, 'There was an error with your submission. Please try again.')
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
                return HttpResponse('Logged In')
            else:
                return HttpResponse('Go away')
        else:
            # Print out the form errors to the console
            print(form.errors)
            # Add an error message to the messages framework
            messages.error(
                request, 'There was an error with your submission. Please try again.')

    dict = {'form': form}
    return render(request, 'loginapp/login.html', dict)
