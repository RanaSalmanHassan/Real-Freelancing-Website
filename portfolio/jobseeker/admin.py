from django.contrib import admin
from .models import Basic_Info,Career_Preference,Contact_Details,Education,Current_Employement,Profile_Pic
# Register your models here.
admin.site.register(Basic_Info)
admin.site.register(Education)
admin.site.register(Contact_Details)
admin.site.register(Current_Employement)
admin.site.register(Career_Preference)
admin.site.register(Profile_Pic)