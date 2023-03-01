from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginapp:login')
def basic_info(request):
    return render(request,'jobseeker/profile/basic_info.html')

@login_required(login_url='loginapp:login')
def education(request):
    return render(request,'jobseeker/profile/education.html')


@login_required(login_url='loginapp:login')
def contact_det(request):
    return render(request, 'jobseeker/profile/contact_det.html')
