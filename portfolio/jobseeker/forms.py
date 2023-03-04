from django import forms
from .models import Profile_Pic

class Profile_Pic_Upload(forms.ModelForm):
    class Meta:
        model = Profile_Pic
        exclude = ('user',)