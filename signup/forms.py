from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_name', 'email', 'major', 'nickname', 'password', 'phone_number']