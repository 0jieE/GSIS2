
from typing import Type
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import post_save
from django.dispatch import receiver

# USERS-------------------------------------------------------------------

class User (AbstractUser,PermissionsMixin):
    id_no = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    extension_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    staff = models.BooleanField(default = False)
    student = models.BooleanField(default = False)
    administrator = models.BooleanField(default = False)
    faculty = models.BooleanField(default = False)

    def __str__(self):
        template = '{0.first_name} {0.middle_name} {0.last_name}'
        return template.format(self)
# ---------------------------------------------------------------------------------------------------------
# ------------------administrator user---------------------------------------------------------------------

class Administrator_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(administrator = True)
    
class Administrator_user(User):
    user = Administrator_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.faculty = False
            self.administrator = True
            self.staff = False
            self.student = False
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            return super().save(*args, **kwargs)

    def welcome(self):
        return "Only for administrator user"
    
@receiver(post_save, sender= Administrator_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.administrator == True:
        Administrator.objects.create(user=instance)


# ---------------------------------------------------------------------------------------------------------
# ------------------faculty user---------------------------------------------------------------------

class Faculty_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(faculty = True)
    
class Faculty_user(User):
    user = Faculty_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.faculty = True
            self.administrator = False
            self.staff = False
            self.student = False
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            return super().save(*args, **kwargs)

    def welcome(self):
        return "Only for faculty user"
    
@receiver(post_save, sender= Faculty_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.faculty == True:
        Faculty.objects.create(user=instance)

# --------------------------------------------------------------------------------------------------------
# -------------------------Staff user--------------------------------------------------------------------------
class Staff_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(staff = True)
    
class Staff_user(User):
    user = Staff_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.faculty = False
            self.administrator = False
            self.staff = True
            self.student = False
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False

            return super().save(*args, **kwargs)

    def welcome(self):
        return "Only for Staff user"
    
@receiver(post_save, sender= Staff_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.staff == True:
        Staff.objects.create(user=instance)

# --------------------------------------------------------------------------------------------------------------------
# --------------------------student_user------------------------------------------------------------------------------

class Student_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(student = True)
    
class Student_user(User):
    user = Student_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.faculty = False
            self.administrator = False
            self.staff = False
            self.student = True
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            
            return super().save(*args, **kwargs)

    def welcome(self):
        return "Only for Student user"
    
@receiver(post_save, sender= Student_user)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.student == True:
        Student.objects.create(user=instance)
      

class Administrator(models.Model):
    user = models.ForeignKey(User, related_name = 'administrator_user_id', on_delete = models.CASCADE)
    contact_number = models.CharField(max_length=50, blank = True, null = True)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null = True, blank = True)
    updated_on = models.DateField(auto_now_add = True)

class Faculty(models.Model):
    user = models.ForeignKey(User, related_name = 'faculty_user_id', on_delete = models.CASCADE)
    contact_number = models.CharField(max_length=50, blank = True, null = True)
    faculty_title = models.CharField(max_length=50, blank = True, null = True)
    faculty_position = models.CharField(max_length=50, blank = True, null = True)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null = True, blank = True)
    updated_on = models.DateField(auto_now_add = True)

    def __str__(self):
        template = '{0.user}'
        return template.format(self)

class Staff(models.Model):
    user = models.ForeignKey(User, related_name = 'staff_user_id', on_delete = models.CASCADE)
    contact_number = models.CharField(max_length=50, blank = True, null = True)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null = True, blank = True)
    updated_on = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    user = models.ForeignKey(User, related_name = 'student_user_id', on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, blank = True, null = True)
    birth_date = models.DateField(blank = True, null = True)
    home_address = models.CharField(max_length=50, blank = True, null = True)
    email_address = models.CharField(max_length=50, blank = True, null = True)
    contact_number = models.CharField(max_length=50, blank = True, null = True)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null = True, blank = True)
    update_on = models.DateField(auto_now_add = True)

#College----------------------------------------------------------------------

class College(models.Model):
    college_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

    def __str__(self):
        template = '{0.college_name}'
        return template.format(self)

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    college = models.ForeignKey(College, related_name ='college_id', on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        template = '{0.department_name}'
        return template.format(self)

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=50)
    course_period = models.IntegerField()
    short_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name="course_department", on_delete = models.CASCADE)

    def __str__(self):
        template = '{0.course_name}'
        return template.format(self)

#Enrollment----------------------------------------------------------------------
    
class Enrollment(models.Model):
    # updated ***
    FIRST = '1st Semester'
    SECOND = '2nd Semester'
    SUMMER = 'Summer'
    SEMESTER = ((FIRST, '1st Semester'), (SECOND,'2nd Semester'), (SUMMER, 'Summer'))

    SY2020 = '2020-2021'
    SY2021 = '2021-2022'
    SY2022 = '2022-2023'
    SY2023 = '2023-2024'
    SY2024 = '2024-2025'
    SY2025 = '2025-2026'
    SY2026 = '2026-2027'
    SY2027 = '2027-2028'
    SY2028 = '2028-2029'
    SY2029 = '2029-2030'
    SY2030 = '2030-2031'
    SCHOOL_YEAR = (
            (SY2020,'2020-2021'),
            (SY2021,'2021-2022'),
            (SY2022,'2022-2023'),
            (SY2023,'2023-2024'),
            (SY2024,'2024-2025'),
            (SY2025,'2025-2026'),
            (SY2026,'2026-2027'),
            (SY2027,'2027-2028'),
            (SY2028,'2028-2029'),
            (SY2029,'2029-2030'),
            (SY2030,'2030-2031')
    )

    enrollment_description = models.CharField(max_length=50)
    semester = models.CharField(max_length=20, choices=SEMESTER, default=FIRST)
    school_year = models.CharField(max_length=10, choices=SCHOOL_YEAR, default=SY2023)

    def __str__(self):
        template = '{0.semester} {0.school_year}'
        return template.format(self)

class Room(models.Model):
    # updated
    LEC = 'Lecture'
    LAB = 'Laboratory'
    ROOOM = (
        (LEC, 'Lecture'), (LAB, 'Laboratory')
    )
    room_no = models.CharField(max_length=50)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=50, choices=ROOOM, default=LEC)
    college = models.ForeignKey(College, related_name = 'college_room', on_delete = models.CASCADE )

    def __str__(self):
        template = '{0.room_no}'
        return template.format(self)

class Subject(models.Model):
    code = models.CharField(max_length=50, unique=True)
    descriptive_title = models.CharField(max_length=250)
    lecture_unit = models.DecimalField(decimal_places = 2, max_digits = 4)
    laboratory_unit = models.DecimalField(decimal_places = 2, max_digits = 4)
    credit_unit = models.DecimalField(decimal_places = 2, max_digits = 4)
    course = models.ForeignKey(Course, related_name='subject_course', on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.code} {0.descriptive_title}'
        # template = '{0.code}'
        return template.format(self)
        # return f'{self.code} - {self.descriptive_title}'

class Class_Schedule(models.Model):
    enrollment = models.ForeignKey(Enrollment, related_name = 'enrollment_class_schedule', on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'subject_class_schedule', on_delete = models.CASCADE)
    room = models.ForeignKey(Room, related_name = 'room_class_schedule', on_delete = models.CASCADE)
    year_level = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty,related_name='faculty_class_schedule',on_delete = models.CASCADE)

    def __str__(self):
        template = '{0.subject}'
        return template.format(self)

class Prospectus(models.Model):
    prospectus_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        template = '{0.prospectus_name}'
        return template.format(self)


class Course_Prospectus(models.Model):
    FIRST = '1st'
    SECOND = '2nd'
    SUMMER = 'Summer'
    SEMESTER = ((FIRST, '1st'), (SECOND,'2nd'), (SUMMER, 'Summer'))

    FIRST_YEAR = '1st Year'
    SECOND_YEAR = '2nd Year'
    THIRD_YEAR = '3rd Year'
    FOURTH_YEAR = '4th Year'
    FIFTH_YEAR = '5th Year'
    YEAR_LEVEL = ((FIRST_YEAR,'1st Year'),
                  (SECOND_YEAR,'2nd Year'),
                  (THIRD_YEAR,'3rd Year'),
                  (FOURTH_YEAR,'4th Year'),
                  (FIFTH_YEAR,'5th Year'),)
    prospectus = models.ForeignKey(Prospectus, related_name = 'course_prospectus_name', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name = 'prospectuse_course_name', on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'prospectus_subject_name', on_delete = models.CASCADE)
    pre_requisit1 = models.ForeignKey(Subject, related_name = 'subject_prereq1', on_delete = models.CASCADE, null=True, blank=True)
    pre_requisit2 = models.ForeignKey(Subject, related_name = 'subject_prereq2', on_delete = models.CASCADE, null=True, blank=True)
    pre_requisit3 = models.ForeignKey(Subject, related_name = 'subject_prereq3', on_delete = models.CASCADE, null=True, blank=True)
    pre_requisit4 = models.ForeignKey(Subject, related_name = 'subject_prereq4', on_delete = models.CASCADE, null=True, blank=True)
    pre_requisit5 = models.ForeignKey(Subject, related_name = 'subject_prereq5', on_delete = models.CASCADE, null=True, blank=True)
    semester = models.CharField(max_length=20, choices=SEMESTER, default=FIRST)
    year_level = models.CharField(max_length=20, choices=YEAR_LEVEL, default=FIRST_YEAR)

class Scholarship(models.Model):
    FULL = 'Full'
    HALF = 'Half'
    NONE = 'None'
    TYPE = (
        (FULL, 'Full'), (HALF, 'Half'), (NONE, 'None')
    )
    scholarship_name = models.CharField(max_length=250)
    scholarship_description = models.CharField(max_length=250)
    scholarship_type = models.CharField(max_length=20, choices=TYPE, default=None)

class Fees(models.Model):
    fee_name = models.CharField(max_length=100, unique=True)
    fee_amount = models.DecimalField(decimal_places = 2, max_digits = 5)
    is_multiplier = models.BooleanField(default=False)

class EnrollmentDetail(models.Model):
    OLD = 'Old Continuing'
    NEW = 'New'
    OS = 'OS'
    TYPE = (
        (OLD, 'Old Continuing'), (NEW, 'New'), (OS, 'OS')
    )

    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    YEAR = (
        (FIRST, '1'), (SECOND, '2'), (THIRD, '3'), (FOURTH, '4')
    )

    ENR = 'Enrolled'
    PRE = 'Pre-Enrolled'
    DRP = 'Dropped'
    PEN = 'Pending'
    STATUS = (
        (ENR, 'Enrolled'), (PRE, 'Pre-Enrolled'), (DRP, 'Dropped'), (PEN, 'Pending')
    )
    student_type = models.CharField(max_length=20, choices=TYPE, default=NEW)
    student_year = models.CharField(max_length=10, choices=YEAR, default=FIRST)
    course_id = models.ForeignKey(Course, related_name='enrollment_detail_course', on_delete=models.DO_NOTHING)
    scholarship_id = models.ForeignKey(Scholarship, related_name='enrollment_detail_scholarship', on_delete=models.DO_NOTHING)
    enrollment_status = models.CharField(max_length=20, choices=STATUS, default=PEN)
    
class SubjectTaken(models.Model):
    schedule_id = models.ForeignKey(Class_Schedule, related_name='subject_taken_schedule', on_delete=DO_NOTHING)
    enrollment_detail_id = models.ForeignKey(EnrollmentDetail, related_name='enrollment_detail', on_delete=models.CASCADE)
    is_pre_enroll = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    is_dropped = models.BooleanField(default=False)
    midterm_grade = models.CharField(max_length=20)
    final_grade = models.CharField(max_length=20)
    final_re_grade = models.CharField(max_length=20)

class Assessment(models.Model):
    enrollment_detail_id = models.ForeignKey(EnrollmentDetail, related_name='enrollment_detail_assessment', on_delete=models.CASCADE)
    fee_id = models.ForeignKey(Fees, related_name='fees', on_delete=models.CASCADE)
    fee_amount = models.DecimalField(decimal_places=2, max_digits=7)
    is_paid = models.BooleanField(default=False)

class Payment(models.Model):
    enrollment_detail_id = models.ForeignKey(EnrollmentDetail, related_name='enrollment_detail_payment', on_delete=models.CASCADE)
    or_no = models.CharField(max_length=20)
    or_date = models.DateTimeField(auto_created=False)
    or_amount = models.DecimalField(decimal_places=2, max_digits=7)

