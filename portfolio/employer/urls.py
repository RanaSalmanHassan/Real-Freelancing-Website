from django.urls import path
from . import views
app_name = 'employer'

urlpatterns = [
    path('create_job_view', views.create_job_view, name='create_job_view')
]
