from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import Create_Job_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='loginapp:login')
def create_job_view(request):
    current_user = request.user
    if current_user.is_admin:
        form = Create_Job_Form()
        if request.method == 'POST':
            form = Create_Job_Form(request.POST,request.FILES)
            if form.is_valid():
                form_instance = form.save(commit=False)
                form_instance.admin = current_user
                form_instance.save()
                messages.success(request, 'Successfully Posted Your Job!')
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(
                    request, 'Please Fill All Compulsory Fields Carefully!')
                return HttpResponseRedirect(reverse('employer:create_job_view'))
        dict = {'form': form}
        return render(request, 'employer/create_job.html', dict)
    else:
        messages.warning(
            request, 'You are not authorised to access this page!')
        return HttpResponse('You cant access this page')
