from . import views
from django.urls import path
app_name = 'loginapp'
urlpatterns = [
    path('login', views.login_page, name='login'),
    path('signup', views.signup, name='signup'),

]
