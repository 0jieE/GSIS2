from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.db.models.fields import files
from .models import Payment, User, Administrator_user, Staff_user, Student_user, College, Department, Course, Enrollment, Room, Subject, Class_Schedule, Prospectus, Course_Prospectus, Student, Staff, Administrator
from django.forms import fields, widgets
from .models import User, Administrator_user, Staff_user, Student_user, \
                    College, Department, Course, Enrollment, Room, Subject, \
                    Class_Schedule, Prospectus, Course_Prospectus, Scholarship, \
                    Fees, EnrollmentDetail, SubjectTaken, Assessment, Payment
from .models import User, Administrator_user, Staff_user, Student_user, College, Department, Course, Enrollment, Room, Subject, Class_Schedule, Prospectus, Course_Prospectus, Student, Staff, Administrator, Faculty_user, Faculty

from django.forms import widgets
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
                "placeholder": "First name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
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
                "placeholder": "First name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
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
                "placeholder": "First name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
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


class FacultyRegistrationForm(UserCreationForm):
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
                "placeholder": "First name",
                "class": "form-control"}))
    
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Middle name",
                "class": "form-control"}))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
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
        model = Faculty_user
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
        widgets ={
            'course_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course name'}),
            'short_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Short name'}),
            'course_period' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Period (i.e. 2)'}),
            'course_description' : forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Description'}),
            'department' : forms.Select(attrs={'class':'form-control'}),
        }

class EnrollmentForm(forms.ModelForm):
    #updated ***
    class Meta:
        model = Enrollment
        fields = ['enrollment_description','semester','school_year','enrollment_ended']
        widgets= {
                'enrollment_description' : forms.Textarea(attrs={'class':'form-control', 'rows': 3, 'placeholder':'Description'}),
                'semester': forms.Select(attrs={'class':'form-control'}),
                'school_year': forms.Select(attrs={'class':'form-control'}),
                
            }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no','capacity','room_type','college']
        widgets = {
            'room_no' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Room no'}),
            'capacity' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Capacity'}),
            'room_type' : forms.Select(attrs={'class':'form-control'}),
            'college' : forms.Select(attrs={'class':'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code','descriptive_title','lecture_unit','laboratory_unit','credit_unit', 'course']
        widgets ={
            'code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course code'}),
            'descriptive_title' : forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Descriptive title'}),
            'lecture_unit' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lec unit'}),
            'laboratory_unit' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lab unit'}),
            'credit_unit' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Credit unit'}),
            'course' : forms.Select(attrs={'class':'form-control'}),
        }

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = Class_Schedule
        fields = ['enrollment','course','subject','room','year_level','schedule','faculty']
        widgets = {
            'enrollment' : forms.Select(attrs={'class':'form-control'}),
            'course' : forms.Select(attrs={'class':'form-control'}),
            'subject' : forms.Select(attrs={'class':'form-control'}),
            'room' : forms.Select(attrs={'class':'form-control'}),
            'year_level' : forms.Select(attrs={'class':'form-control'}),
            'schedule' : forms.TextInput(attrs={'class':'form-control','placeholder':'Schedule (ie. TTH - 1:00PM-3:00PM, MWF - 7:00AM - 9:00AM'}),
            'faculty' : forms.Select(attrs={'class':'form-control',}),
        }

class PropectuseForm(forms.ModelForm):
    class Meta:
        model = Prospectus
        fields = ['prospectus_name','description']
        widgets = {
            'prospectus_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prospectus name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Description'})
        }

class CoursePropectuseform(forms.ModelForm):
    class Meta:
        model = Course_Prospectus
        fields = ['prospectus','course','subject','pre_requisit1','pre_requisit2','pre_requisit3','pre_requisit4','pre_requisit5','semester','year_level']

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = ['scholarship_name', 'scholarship_description', 'scholarship_type']
        widgets = {
            'scholarship_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scholarship'}),
            'scholarship_description' : forms.Textarea(attrs={'class':'form-control', 'row':3, 'placeholder':'Description'}),
            'scholarship_type' : forms.Select(attrs={'class':'form-control'})
        }

class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = ['fee_name', 'fee_amount', 'is_multiplier']
        widgets = {
            'fee_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fee name'}),
            'fee_amount' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Amount'}),
            'is_multiplier' : forms.CheckboxInput(attrs={'class':'form-control'})
        }

class EnrollmentDetailForm(forms.ModelForm):
    class Meta:
        model = EnrollmentDetail
        fields = ['enrollment','student','student_type', 'student_year', 'course_id', 'scholarship_id', 'enrollment_status']
        widgets = {
            'enrollment' : forms.Select(attrs={'class':'form-control'}),
            'student' : forms.Select(attrs={'class':'form-control'}),
            'student_type' : forms.Select(attrs={'class':'form-control'}),
            'student_year' : forms.Select(attrs={'class':'form-control'}),
            'course_id' : forms.Select(attrs={'class':'form-control'}),
            'scholarhip_id' : forms.Select(attrs={'class':'form-control'}),
            'enrollment_status' : forms.Select(attrs={'class':'form-control'})
        }

class StudentPreEnrollmentForm(forms.ModelForm):
    class Meta:
        model = EnrollmentDetail
        fields = ['enrollment','student','student_type', 'student_year', 'course_id', 'scholarship_id', 'enrollment_status']
        widgets = {
            'enrollment' : forms.HiddenInput(),
            'student' : forms.HiddenInput(),
            'student_type' : forms.Select(attrs={'class':'form-control'}),
            'student_year' : forms.Select(attrs={'class':'form-control'}),
            'course_id' : forms.Select(attrs={'class':'form-control'}),
            'scholarhip_id' : forms.Select(attrs={'class':'form-control'}),
            'enrollment_status' : forms.Select(attrs={'class':'form-control'})
        }

class SubjectTakenForm(forms.ModelForm):
    class Meta:
        model = SubjectTaken
        fields = ['schedule_id', 'enrollment_detail_id','is_pre_enroll','is_registered', 'is_dropped', 'midterm_grade', 'final_grade', 'final_re_grade']


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['enrollment_detail_id', 'fee_id', 'fee_amount', 'is_paid']

    def __init__(self, *args, **kwargs):
        super(AssessmentForm, self).__init__(*args, **kwargs)
        self.fields['enrollment_detail_id'].widget.attrs['onchange'] = 'calculate_fee_amount()'
        self.fields['fee_id'].widget.attrs['onchange'] = 'calculateFeeAmount()'

    def save(self, commit=True):
        assessment = super(AssessmentForm, self).save(commit=False)
        enrollment_detail_id = self.cleaned_data['enrollment_detail_id']
        fee_id = self.cleaned_data['fee_id']

        # Calculate fee_amount based on the conditions
        if fee_id.is_multiplier:
            # Fetch the total number of credit_unit of the Subject based on EnrollmentDetail and SubjectTaken and Subject
            total_credit_units = self.calculate_total_credit_units(enrollment_detail_id)
            fee_amount = fee_id.fee_amount * total_credit_units
            assessment.fee_amount = fee_amount
        else:
            assessment.fee_amount = fee_id.fee_amount

        if commit:
            assessment.save()
        return assessment

    def calculate_total_credit_units(self, enrollment_detail_id):
        # Implement your logic to calculate total credit units based on EnrollmentDetail and SubjectTaken
        # This could involve querying related models to sum up credit units
        # For demonstration, let's assume a simple calculation
        total_credit_units = 0
        # Fetch related SubjectTaken objects based on enrollment_detail_id
        subject_taken_list = SubjectTaken.objects.filter(enrollment_detail_id=enrollment_detail_id)
        for subject_taken in subject_taken_list:
            total_credit_units += subject_taken.schedule_id.subject.credit_unit
        return total_credit_units

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['enrollment_detail_id', 'or_no', 'or_date', 'or_amount']
        widgets = {
            'enrollment_detail_id' : forms.Select(attrs={'class':'form-control'}),
            'or_no' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'OR no'}),
            'or_date' : forms.DateTimeInput(attrs={'class':'form-control'}),
        }

# user profiles

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email_address','gender','birth_date','home_address','contact_number']

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['contact_number',]

class AdministratorProfileForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['contact_number',]

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['contact_number','faculty_title','faculty_position',]

class StudentAccountEditForm(forms.ModelForm):
    class Meta:
        model = Student_user
        fields = ('username','first_name','middle_name','last_name','id_no')

class StaffAccountEditForm(forms.ModelForm):
    class Meta:
        model = Staff_user
        fields = ('username','first_name','middle_name','last_name','id_no')

class AdministratorAccountEditForm(forms.ModelForm):
    class Meta:
        model = Administrator_user
        fields = ('username','first_name','middle_name','last_name','id_no')

class FacultyAccountEditForm(forms.ModelForm):
    class Meta:
        model = Faculty_user
        fields = ('username','first_name','middle_name','last_name','id_no')

