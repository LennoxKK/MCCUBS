
from .models import User
from django import forms
from xml.dom import ValidationErr
from django.contrib.auth.models import User as Ad
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,UserProfile


class UserRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'sir_middle_name',
            'reg_no',
            'level',
            'phone_number',
            'place_of_residence',
            'gender'
        ]


    def clean_level(self, *args, **kwargs):
        level = self.cleaned_data.get('level')
        if level != None:
            if level > 6 or level < 1:
                print(level)
                raise forms.ValidationError(f'Level is between  1 and 6!')
            return level
        else:
            raise ValidationErr(f"Please fill the year of study field")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Ad
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Ad
        fields = ['username', 'email']
# Create a UserUpdateForm to update a username and email
class CUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']