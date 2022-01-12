from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
# from django.contrib.auth.models import StudentInfo
from .models import StudentInfo
from .models import StudentAcademics


class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('username','first_name','last_name','email','password1', 'password2')
        model = User

    def __init__(self,*args,**kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)
        self.fields['password2'].label = 'Confirm Password (again)'
        self.fields['email'].label = 'Email'
        self.fields['username']
        self.fields['first_name']
        self.fields['email']
        self.fields['password1']
        self.fields['password2']
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username']
        self.fields['password']



class StudentsForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        # fields = ["rollNo", "name", "student_class", "school", "mobile", "address"]
        fields = "__all__"


class StudentsAcademicsForm(forms.ModelForm):
    class Meta:
        model = StudentAcademics
        # fields = "__all__"
        fields = ["rollNo" ,"maths", "physics", "chemistry", "biology","english"]
        