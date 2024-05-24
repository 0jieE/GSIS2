
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm,AdministratorRegistrationForm, StaffRegistrationForm, StudentRegistrationForm, RegistrationForm, DepartmentForm, CourseForm, CollegeForm, EnrollmentForm, RoomForm, SubjectForm, ClassScheduleForm, PropectuseForm, CoursePropectuseform
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, authenticate,login
from .models import College, Department, Course, Enrollment, Room, Subject, Class_Schedule, Prospectus, Course_Prospectus


from django.contrib.auth.decorators import login_required

from .models import *

def index(request):
  if not request.user.is_authenticated:
    return redirect("login/")
  else:
    context = {
      'segment'  : 'index',
      #'products' : Product.objects.all()
    }
    return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.administrator:
                login(request, user)
                return redirect('/administrator/enrollment/list')
            elif user is not None and user.staff:
                login(request, user)
                return redirect('/administrator/enrollment/list')
            elif user is not None and user.student:
                login(request, user)
                return redirect('/student/home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/auth-signin.html', {'form': form, 'msg': msg})

class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

def register_administrator(request):
    msg = None
    success = False
    if request.method == "POST":
        form = AdministratorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = AdministratorRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def register_staff(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def register_student(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def logout_view(request):
  logout(request)
  return redirect('login/')

def administrator(request):
    
    return render(request, 'administrator/admnstr_home.html')

def staff(request):
    
    return render(request, 'staff/staff_home.html')

def student(request):
    
    return render(request, 'student/student_home.html')

def user_profile(request):
    
    return render(request, 'accounts/user_profile.html')

#///////////////////////////////CRUDE ADMINISTRATOR/////////////////////////////////////////////////////////////

#________________________________________________________________________________________________________


                        #------------department Views---------------#

#________________________________________________________________________________________________________


def department(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        departments = Department.objects.all()
        context = {
                'parent': 'college_unit',
                'segment': 'department',
                'departments':departments,
        }
    return render(request, 'administrator/department/departments.html',context)

def add_department(request):
        if(request.method == 'POST'):
                form = DepartmentForm(request.POST)
        else:    
                form = DepartmentForm()

        return save_department(request, form, 'administrator/department/add_department.html')


def edit_department(request,pk):
        department = get_object_or_404(Department, pk=pk)
        if(request.method == 'POST'):
                form = DepartmentForm(request.POST, instance=department)
        else:    
                form = DepartmentForm(instance=department)
        return save_department(request, form, 'administrator/department/edit_department.html')


def delete_department(request,pk):
        department = get_object_or_404(Department, pk=pk)
        data = dict()
        if request.method == 'POST':
            department.delete()
            data['form_is_valid'] = True
            departments= Department.objects.all()
            data['department_list'] = render_to_string('administrator/department/list_department.html',{'departments':departments})
        else:    
            context = {'department':department}
            data['html_form'] = render_to_string('administrator/department/delete_department.html',context,request=request)
        return JsonResponse(data)


def save_department(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        departments= Department.objects.all()
        data['department_list'] = render_to_string('administrator/department/list_department.html',{'departments':departments})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------college Views---------------#

#________________________________________________________________________________________________________


def college(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        colleges = College.objects.all()
        context = {
              'parent':'college_unit',
              'segment':'college',
              'colleges': colleges,
        }
        return render(request, 'administrator/college/college.html',context)

def add_college(request):
        if(request.method == 'POST'):
                form = CollegeForm(request.POST)
        else:    
                form = CollegeForm()

        return save_college(request, form, 'administrator/college/add_college.html')


def edit_college(request,pk):
        college = get_object_or_404(College, pk=pk)
        if(request.method == 'POST'):
                form = CollegeForm(request.POST, instance=college)
        else:    
                form = CollegeForm(instance=college)
        return save_college(request, form, 'administrator/college/edit_college.html')


def delete_college(request,pk):
        college = get_object_or_404(College, pk=pk)
        data = dict()
        if request.method == 'POST':
            college.delete()
            data['form_is_valid'] = True
            colleges= College.objects.all()
            data['college_list'] = render_to_string('administrator/college/list_college.html',{'colleges':colleges})
        else:    
            context = {'college':college}
            data['html_form'] = render_to_string('administrator/college/delete_college.html',context,request=request)
        return JsonResponse(data)


def save_college(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        colleges= College.objects.all()
        data['college_list'] = render_to_string('administrator/college/list_college.html',{'colleges':colleges})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------course Views---------------#

#________________________________________________________________________________________________________


def course(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        courses = Course.objects.all()
        departments = Department.objects.all()
        context = {
                'parent': 'college_unit',
                'segment': 'courses',
                'courses':courses,
        }
        return render(request, 'administrator/course/course.html',context)

def add_course(request):
        if(request.method == 'POST'):
                form = CourseForm(request.POST)
        else:    
                form = CourseForm()

        return save_course(request, form, 'administrator/course/add_course.html')


def edit_course(request,pk):
        course = get_object_or_404(Course, pk=pk)
        if(request.method == 'POST'):
                form = CourseForm(request.POST, instance=course)
        else:    
                form = CourseForm(instance=course)
        return save_course(request, form, 'administrator/course/edit_course.html')


def delete_course(request,pk):
        course = get_object_or_404(Course, pk=pk)
        data = dict()
        if request.method == 'POST':
            course.delete()
            data['form_is_valid'] = True
            courses= Course.objects.all()
            data['course_list'] = render_to_string('administrator/course/list_course.html',{'courses':courses})
        else:    
            context = {'course':course}
            data['html_form'] = render_to_string('administrator/course/delete_course.html',context,request=request)
        return JsonResponse(data)


def save_course(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        courses= Course.objects.all()
        data['course_list'] = render_to_string('administrator/course/list_course.html',{'courses':courses})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Enrollment Views---------------#

#________________________________________________________________________________________________________


def enrollment(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        enrollments = Enrollment.objects.all()
        context = {
                'parent':'',
                'segment': 'enrollments',
                'enrollments':enrollments
        }
    return render(request, 'administrator/enrollment/enrollment.html', context)

def add_enrollment(request):
        if(request.method == 'POST'):
                form = EnrollmentForm(request.POST)
        else:    
                form = EnrollmentForm()

        return save_enrollment(request, form, 'administrator/enrollment/add_enrollment.html')


def edit_enrollment(request,pk):
        enrollment = get_object_or_404(Enrollment, pk=pk)
        if(request.method == 'POST'):
                form = EnrollmentForm(request.POST, instance=enrollment)
        else:    
                form = EnrollmentForm(instance=enrollment)
        return save_enrollment(request, form, 'administrator/enrollment/edit_enrollment.html')


def delete_enrollment(request,pk):
        enrollment = get_object_or_404(Enrollment, pk=pk)
        data = dict()
        if request.method == 'POST':
            enrollment.delete()
            data['form_is_valid'] = True
            enrollments= Enrollment.objects.all()
            data['enrollment_list'] = render_to_string('administrator/enrollment/list_enrollment.html',{'enrollments':enrollments})
        else:    
            context = {'enrollment':enrollment}
            data['html_form'] = render_to_string('administrator/enrollment/delete_enrollment.html',context,request=request)
        return JsonResponse(data)


def save_enrollment(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        enrollments= Enrollment.objects.all()
        data['enrollment_list'] = render_to_string('administrator/enrollment/list_enrollment.html',{'enrollments':enrollments})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Room Views---------------#

#________________________________________________________________________________________________________


def room(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        rooms = Room.objects.all()
        context = {
              'segment':'room',
              'rooms':rooms
        }
        return render(request, 'administrator/room/room.html',context)

def add_room(request):
        if(request.method == 'POST'):
                form = RoomForm(request.POST)
        else:    
                form = RoomForm()

        return save_room(request, form, 'administrator/room/add_room.html')


def edit_room(request,pk):
        room = get_object_or_404(Room, pk=pk)
        if(request.method == 'POST'):
                form = RoomForm(request.POST, instance=room)
        else:    
                form = RoomForm(instance=room)
        return save_room(request, form, 'administrator/room/edit_room.html')


def delete_room(request,pk):
        room = get_object_or_404(Room, pk=pk)
        data = dict()
        if request.method == 'POST':
            room.delete()
            data['form_is_valid'] = True
            rooms= Room.objects.all()
            data['room_list'] = render_to_string('administrator/room/list_room.html',{'rooms':rooms})
        else:    
            context = {'room':room}
            data['html_form'] = render_to_string('administrator/room/delete_room.html',context,request=request)
        return JsonResponse(data)


def save_room(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        rooms= Room.objects.all()
        data['room_list'] = render_to_string('administrator/room/list_room.html',{'rooms':rooms})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------subject Views---------------#

#________________________________________________________________________________________________________


def subject(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        subjects = Subject.objects.all()
        context = {
                'parent': 'prospectus_',
                'segment': 'subject',
                'subjects':subjects,
        }
        return render(request, 'administrator/subject/subject.html',context)

def add_subject(request):
        if(request.method == 'POST'):
                form = SubjectForm(request.POST)
        else:    
                form = SubjectForm()

        return save_subject(request, form, 'administrator/subject/add_subject.html')


def edit_subject(request,pk):
        subject = get_object_or_404(Subject, pk=pk)
        if(request.method == 'POST'):
                form = SubjectForm(request.POST, instance=subject)
        else:    
                form = SubjectForm(instance=subject)
        return save_subject(request, form, 'administrator/subject/edit_subject.html')


def delete_subject(request,pk):
        subject = get_object_or_404(Subject, pk=pk)
        data = dict()
        if request.method == 'POST':
            subject.delete()
            data['form_is_valid'] = True
            subjects= Subject.objects.all()
            data['subject_list'] = render_to_string('administrator/subject/list_subject.html',{'subjects':subjects})
        else:    
            context = {'subject':subject}
            data['html_form'] = render_to_string('administrator/subject/delete_subject.html',context,request=request)
        return JsonResponse(data)


def save_subject(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        subjects= Subject.objects.all()
        data['subject_list'] = render_to_string('administrator/subject/list_subject.html',{'subjects':subjects})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Class Schedule Views---------------#

#________________________________________________________________________________________________________


def class_schedule(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        class_schedules = Class_Schedule.objects.all()
        context = {
          'parent': 'enrollment',
          'segment': 'class_schedule',
          'class_schedules':class_schedules,
    }
        return render(request, 'administrator/class_schedule/class_schedule.html',context)

def add_class_schedule(request):
        if(request.method == 'POST'):
                form = ClassScheduleForm(request.POST)
        else:    
                form = ClassScheduleForm()

        return save_class_schedule(request, form, 'administrator/class_schedule/add_class_schedule.html')


def edit_class_schedule(request,pk):
        class_schedule = get_object_or_404(Class_Schedule, pk=pk)
        if(request.method == 'POST'):
                form = ClassScheduleForm(request.POST, instance=class_schedule)
        else:    
                form = ClassScheduleForm(instance=class_schedule)
        return save_class_schedule(request, form, 'administrator/class_schedule/edit_class_schedule.html')


def delete_class_schedule(request,pk):
        class_schedule = get_object_or_404(Class_Schedule, pk=pk)
        data = dict()
        if request.method == 'POST':
            class_schedule.delete()
            data['form_is_valid'] = True
            class_schedules= Class_Schedule.objects.all()
            data['class_schedule_list'] = render_to_string('administrator/class_schedule/list_class_schedule.html',{'class_schedules':class_schedules})
        else:    
            context = {'class_schedule':class_schedule}
            data['html_form'] = render_to_string('administrator/class_schedule/delete_class_schedule.html',context,request=request)
        return JsonResponse(data)


def save_class_schedule(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        class_schedules= Class_Schedule.objects.all()
        data['class_schedule_list'] = render_to_string('administrator/class_schedule/list_class_schedule.html',{'class_schedules':class_schedules})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Prospectus Views---------------#

#________________________________________________________________________________________________________


def prospectus(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        prospectus = Prospectus.objects.all()
        context = {
              'parent':'prospectus_',
              'segment':'prospectus',
              'prospectus':prospectus,          
        }
        return render(request, 'administrator/prospectus/prospectus.html',context)

def add_prospectus(request):
        if(request.method == 'POST'):
                form = PropectuseForm(request.POST)
        else:    
                form = PropectuseForm()

        return save_prospectus(request, form, 'administrator/prospectus/add_prospectus.html')


def edit_prospectus(request,pk):
        prospectus = get_object_or_404(Prospectus, pk=pk)
        if(request.method == 'POST'):
                form = PropectuseForm(request.POST, instance=prospectus)
        else:    
                form = PropectuseForm(instance=prospectus)
        return save_prospectus(request, form, 'administrator/prospectus/edit_prospectus.html')


def delete_prospectus(request,pk):
        prospectus = get_object_or_404(Prospectus, pk=pk)
        data = dict()
        if request.method == 'POST':
            prospectus.delete()
            data['form_is_valid'] = True
            prospectus= Prospectus.objects.all()
            data['prospectus_list'] = render_to_string('administrator/prospectus/list_prospectus.html',{'prospectus':prospectus})
        else:    
            context = {'prospectus':prospectus}
            data['html_form'] = render_to_string('administrator/prospectus/delete_prospectus.html',context,request=request)
        return JsonResponse(data)


def save_prospectus(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        prospectus= Prospectus.objects.all()
        data['prospectus_list'] = render_to_string('administrator/prospectus/list_prospectus.html',{'prospectus':prospectus})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Course Prospectus Views---------------#

#________________________________________________________________________________________________________


def course_prospectus(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        course_prospectus = Course_Prospectus.objects.all()
        context = {
              'parent':'prospectus_',
              'segment':'course_p',
              'course_prospectus':course_prospectus,        
        }
        return render(request, 'administrator/course_prospectus/course_prospectus.html',context)

def add_course_prospectus(request):
        if(request.method == 'POST'):
                form = CoursePropectuseform(request.POST)
        else:    
                form = CoursePropectuseform()

        return save_course_prospectus(request, form, 'administrator/course_prospectus/add_course_prospectus.html')


def edit_course_prospectus(request,pk):
        course_prospectus = get_object_or_404(Course_Prospectus, pk=pk)
        if(request.method == 'POST'):
                form = CoursePropectuseform(request.POST, instance=course_prospectus)
        else:    
                form = CoursePropectuseform(instance=course_prospectus)
        return save_course_prospectus(request, form, 'administrator/course_prospectus/edit_course_prospectus.html')


def delete_course_prospectus(request,pk):
        course_prospectus = get_object_or_404(Course_Prospectus, pk=pk)
        data = dict()
        if request.method == 'POST':
            course_prospectus.delete()
            data['form_is_valid'] = True
            course_prospectus= Course_Prospectus.objects.all()
            data['course_prospectus_list'] = render_to_string('administrator/course_prospectus/list_course_prospectus.html',{'course_prospectus':course_prospectus})
        else:    
            context = {'course_prospectus':course_prospectus}
            data['html_form'] = render_to_string('administrator/course_prospectus/delete_course_prospectus.html',context,request=request)
        return JsonResponse(data)


def save_course_prospectus(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        course_prospectus= Course_Prospectus.objects.all()
        data['course_prospectus_list'] = render_to_string('administrator/course_prospectus/list_course_prospectus.html',{'course_prospectus':course_prospectus})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)