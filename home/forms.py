from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from .models import User, Administrator_user, Staff_user, Student_user, College, Department, Course, Enrollment, Room, Subject, Class_Schedule, Prospectus, Course_Prospectus
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
  )
  password2 = forms.CharField(
      label=_("Confirm Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
  )

  class Meta:
    model = User
    fields = ('username', 'email', )

    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Username'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'Email'
      })
    }



class AdministratorRegistrationForm(UserCreationForm):
    id_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ID number",
                "class": "form-control"}))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))

    class Meta:
        model = Administrator_user
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2','id_no')


class StaffRegistrationForm(UserCreationForm):
    id_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ID number",
                "class": "form-control"}))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))

    class Meta:
        model = Staff_user
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2','id_no')

class StudentRegistrationForm(UserCreationForm):
    id_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ID number",
                "class": "form-control"}))

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"}))
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"}))
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"}))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"}))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"}))

    class Meta:
        model = Student_user
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2','id_no')



class LoginForm(forms.Form):
  username = UsernameField(label=_("Your Username"), widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(
      label=_("Your Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
  )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Old Password'
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name','short_name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name','short_name','college']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','short_name','course_description','course_period','department']

class EnrollmentForm(forms.ModelForm):
    #updated ***
    class Meta:
        model = Enrollment
        fields = ['enrollment_description','semester','school_year']
        widgets= {
                'enrollment_description' : forms.Textarea(attrs={'class':'forms-control-sm', 'rows': 3, 'placeholder':'Description'}),
                'semester': forms.Select(attrs={'class':'form-control-sm'}),
                'school_year': forms.Select(attrs={'class':'form-control-sm'}),
            }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no','capacity','room_type','college']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code','descriptive_title','lecture_unit','laboratory_unit','credit_unit']

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = Class_Schedule
        fields = ['enrollment','subject','room','year_level','schedule']

class PropectuseForm(forms.ModelForm):
    class Meta:
        model = Prospectus
        fields = ['prospectus_name','description']

class CoursePropectuseform(forms.ModelForm):
    class Meta:
        model = Course_Prospectus
        fields = ['prospectus','course','subject','pre_requisit1','pre_requisit2','pre_requisit3','pre_requisit4','pre_requisit5','semester','year_level']