from django import forms
from django.forms import ModelForm
from django.forms import fields
from django.forms.models import fields_for_model
from user.models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['Full_name','Profile_image','Email_ID','Short_description','Long_description','Degree','Year_of_passing','Certificate_image',]

        widgets = {
            'Full_name' : forms.TextInput(attrs={'class':'form-control'}),
            'Profile_image' : forms.FileInput(attrs={'class':'form-control'}),
            'Email_ID' : forms.EmailInput(attrs={'class':'form-control'}),
            'Short_description' : forms.Textarea(attrs={'class':'form-control'}),
            'Long_description' : forms.Textarea(attrs={'class':'form-control'}),
            'Degree' : forms.TextInput(attrs={'class':'form-control'}),
            'Year_of_passing' : forms.NumberInput(attrs={'class':'form-control'}),
            'Certificate_image' : forms.FileInput(attrs={'class':'form-control'}),
           
            

        }       
