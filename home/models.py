
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
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

    def __str__(self):
        template = '{0.first_name} {0.middle_name} {0.last_name}'
        return template.format(self)


class Administrator_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(Administrator = True)
    
class Administrator_user(User):
    user = Administrator_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
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

class Staff_user_manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset( *args, **kwargs)
        return results.filter(Staff = True)
    
class Staff_user(User):
    user = Staff_user_manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
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
    department = models.ForeignKey(Department, related_name = 'course_department_name', on_delete = models.CASCADE)
    def __str__(self):
        template = '{0.course_name}'
        return template.format(self)

#Enrollment----------------------------------------------------------------------
    
class Enrollment(models.Model):
    # updated ***
    FIRST = '1st'
    SECOND = '2nd'
    SUMMER = 'Summer'
    SEMESTER = ((FIRST, '1st'), (SECOND,'2nd'), (SUMMER, 'Summer'))

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
    semester = models.CharField(max_length=10, choices=SEMESTER, default=FIRST)
    school_year = models.CharField(max_length=10, choices=SCHOOL_YEAR, default=SY2023)

    def __str__(self):
        template = '{0.semester} {0.school_year}'
        return template.format(self)

class Room(models.Model):
    room_no = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)
    college = models.ForeignKey(College, related_name = 'college_room', on_delete = models.CASCADE )

    def __str__(self):
        template = '{0.room_no}'
        return template.format(self)

class Subject(models.Model):
    code = models.CharField(max_length=50)
    descriptive_title = models.CharField(max_length=50)
    lecture_unit = models.DecimalField(decimal_places = 2, max_digits = 4)
    laboratory_unit = models.DecimalField(decimal_places = 2, max_digits = 4)
    credit_unit = models.DecimalField(decimal_places = 2, max_digits = 4)

    def __str__(self):
        template = '{0.code} {0.descriptive_title}'
        return template.format(self)

class Class_Schedule(models.Model):
    enrollment = models.ForeignKey(Enrollment, related_name = 'enrollment_class_schedule', on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'subject_class_schedule', on_delete = models.CASCADE)
    room = models.ForeignKey(Room, related_name = 'room_class_schedule', on_delete = models.CASCADE)
    year_level = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)

    def __str__(self):
        template = '{0.subject}'
        return template.format(self)

class Prospectus(models.Model):
    prospectus_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        template = '{0.prospectus_name}'
        return template.format(self)


class Course_Prospectus(models.Model):
    prospectus = models.ForeignKey(Prospectus, related_name = 'course_prospectus_name', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name = 'prospectuse_course_name', on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = 'prospectus_subject_name', on_delete = models.CASCADE)
    pre_requisit1 = models.ForeignKey(Subject, related_name = 'subject_prereq1', on_delete = models.CASCADE)
    pre_requisit2 = models.ForeignKey(Subject, related_name = 'subject_prereq2', on_delete = models.CASCADE)
    pre_requisit3 = models.ForeignKey(Subject, related_name = 'subject_prereq3', on_delete = models.CASCADE)
    pre_requisit4 = models.ForeignKey(Subject, related_name = 'subject_prereq4', on_delete = models.CASCADE)
    pre_requisit5 = models.ForeignKey(Subject, related_name = 'subject_prereq5', on_delete = models.CASCADE)
    semester = models.IntegerField()
    year_level = models.CharField(max_length=50)


