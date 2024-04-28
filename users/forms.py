from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.forms import CloudinaryFileField
from .models import Profile


class UploadProfilePhotoForm(forms.ModelForm):
    image = CloudinaryFileField(label="Profile Photo", required=True)
    
    class Meta:
        model = Profile
        fields = ['image']
        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    
    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username alreay exists")
        return username
    
    
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email alreay exists")
        return email
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            "email": forms.EmailInput(attrs={'class': 'form-control form-control-lg border-primary'}),
        }