from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_name', 'email', 'major', 'nickname', 'phone_number']
