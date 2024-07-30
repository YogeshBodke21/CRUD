from .models import StudentInfo
from django import forms 
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus":"True", "class":"form-control"})),
    email = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus":"True", "class":"form-control"})),
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control"})),
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class StudentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = StudentInfo
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "Mobile_No":forms.NumberInput( attrs={"class":"form-control"}),
            "Fee":forms.NumberInput(attrs={"class":"form-control"}),
            "Address":forms.TextInput(attrs={"class":"form-control"}),
        }