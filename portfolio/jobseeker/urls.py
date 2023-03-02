from django.urls import path
from . import views
app_name ='jobseeker'
urlpatterns = [
    path('profile/basic_info',views.basic_info,name='profile/basic_info'),
    path('profile/education',views.education,name='profile/education'),
    path('profile/contact_det', views.contact_det, name='profile/contact_det'),
    path('profile/current_emp', views.current_emp, name='profile/current_emp'),
    path('profile/career_pref', views.career_pref, name='profile/career_pref'),
]