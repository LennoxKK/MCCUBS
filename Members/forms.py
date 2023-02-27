
from .models import Member
from django import forms


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name',
            'sir_middle_name',
            'reg_no',
            'level',
            'phone_number',
            'place_of_residence',
        ]

        widgets = {
            "level": forms.NumberInput(attrs={"class": "input-field", "placeholder": "year of study"}),
            # "gender":forms.RadioSelect(attrs={"class":"input-field"}),
            # "leader_status":forms.CheckboxInput(attrs={"class":"input-field","placeholder":"Want to be a bs leader?"}),
            "first_name": forms.TextInput(attrs={"class": "input-field", "placeholder": "first name"}),
            "sir_midlle_name": forms.TextInput(attrs={"class": "input-field", "placeholder": "sir name"}),
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
            "sir_middle_name": ""
        }
