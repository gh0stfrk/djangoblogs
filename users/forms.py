from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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