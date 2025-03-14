from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

# Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        valid_domains = ('@gmail.com', '@yahoo.com', '@mail.com', '@google.com', '@icloud.com', '@outlook.com')
        if not email.endswith(valid_domains):
            raise ValidationError('Please use a valid email address.')
        return email

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create record
class CreateRecordForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        valid_domains = ('@gmail.com', '@yahoo.com', '@mail.com', '@google.com', '@icloud.com', '@outlook.com')
        if not email.endswith(valid_domains):
            raise ValidationError('Please use a valid email address.')
        return email

# Update record
class UpdateRecordForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        valid_domains = ('@gmail.com', '@yahoo.com', '@mail.com', '@google.com', '@icloud.com', '@outlook.com')
        if not email.endswith(valid_domains):
            raise ValidationError('Please use a valid email address.')
        return email
