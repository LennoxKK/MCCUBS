
from .models import User
from django import forms
from xml.dom import ValidationErr


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

        widgets = {
            "level": forms.NumberInput(attrs={"class": "input-field", "placeholder": "year of study"}),
            # "gender":forms.RadioSelect(attrs={"class":"input-field"}),
            # "leader_status":forms.CheckboxInput(attrs={"class":"input-field","placeholder":"Want to be a bs leader?"}),
            "first_name": forms.TextInput(attrs={"class": "input-field", "placeholder": "first name"}),
            "sir_middle_name": forms.TextInput(attrs={"class": "input-field", "placeholder": "sir name"}),
            "phone_number": forms.TextInput(attrs={"class": "input-field", "placeholder": "Phone number"}),
            "sir_middle_name": forms.TextInput(attrs={"class": "input-field", "placeholder": "Other Two"}),
            "reg_no": forms.TextInput(attrs={"class": "input-field", "placeholder": "Reg No"}),

        }

        labels = {

            "first_name": "",
            "level": "",
            "sir_name": "",
            "phone_number": "",
            "reg_no": "",
            "place_of_residence": "",
            "sir_middle_name": "",
            'gender': ''
        }

    def clean_level(self, *args, **kwargs):
        level = self.cleaned_data.get('level')
        if level != None:
            if level > 6 or level < 1:
                print(level)
                raise forms.ValidationError(f'Level is between  1 and 6!')
            return level
        else:
            raise ValidationErr(f"Please fill the year of study field")
